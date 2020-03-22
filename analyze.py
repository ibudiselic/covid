import csv
import datetime
import math
import matplotlib.pyplot as plt

from collections import defaultdict
from scipy.optimize import curve_fit

KEY_COUNTRY = 1
KEY_DATES_START = 4

# Returns a proper `datetime` from `date_str` in a format like
# '1/22/20', which represents January 22nd, 2020.
def make_date(date_str):
    parts = date_str.split('/')
    assert(len(parts) == 3)
    return datetime.date(2000 + int(parts[2]), int(parts[0]), int(parts[1]))

class DayData(object):
    def __init__(self, confirmed, recovered, dead):
        self.confirmed = confirmed
        self.recovered = recovered
        self.dead = dead

    def __repr__(self):
        return 'c: {}, r: {}, d: {}'.format(self.confirmed, self.recovered, self.dead)

class Country(object):
    def __init__(self, name, population, kind_data):
        self.name = name
        self.population = population
        self.timeseries = [DayData(confirmed, recovered, dead)
            for confirmed, recovered, dead in
                zip(kind_data['confirmed'], kind_data['recovered'], kind_data['dead'])]

    def __repr__(self):
        return '{}: [{}]'.format(self.name, ', '.join(str(dd) for dd in self.timeseries))

    def _project(self, perm, dayfn):
        factor = 1000.0/self.population if perm else 1.0
        return [dayfn(day) * factor for day in self.timeseries]

    def confirmed(self, perm=False):
        return self._project(perm, lambda day: day.confirmed)

    def recovered(self, perm=False):
        return self._project(perm, lambda day: day.recovered)

    def dead(self, perm=False):
        return self._project(perm, lambda day: day.dead)

    def dispatch(self, series, perm=False):
        if series == 'confirmed':
            return self.confirmed(perm)
        elif series == 'recovered':
            return self.recovered(perm)
        elif series == 'dead':
            return self.dead(perm)
        else:
            raise Exception('unknown method in disppatch: ' + statname)

def read_one_data_kind(kind):
    country_data = dict()
    with open('data/{}.csv'.format(kind)) as fin:
        reader = csv.reader(fin, delimiter=',', quotechar='"')
        header = next(reader)
        dates = [make_date(date_str) for date_str in header[KEY_DATES_START:]]
        for line in reader:
            name = line[KEY_COUNTRY]
            vals = [int(v) for v in line[KEY_DATES_START:]]
            assert(len(vals) == len(dates))
            if name not in country_data:
                country_data[name] = vals
            else:
                # Another province/state for the same country.
                # We just sum this up.
                cur = country_data[name]
                assert(len(cur) == len(vals))
                for i in range(len(cur)):
                    cur[i] += vals[i]
    return dates, country_data

class DB(object):
    def __init__(self):
        self.dates = None
        # {country -> kind -> numbers}
        per_country = defaultdict(dict)
        for kind in ['confirmed', 'recovered', 'dead']:
            dates, country_data = read_one_data_kind(kind)
            if self.dates is None:
                self.dates = dates
            else:
                # We're assuming all the dates are present in all the datasets.
                assert(self.dates == dates)
            if len(per_country) > 0:
                assert(set(per_country.keys()) == set(country_data.keys()))
            for country, vals in country_data.items():
                per_country[country][kind] = vals

        # {country name -> population}
        populations = dict()
        with open('data/country_population.txt') as fin:
            for line in fin:
                parts = line.split(' ')
                populations[' '.join(parts[:-1])] = int(parts[-1])
        self.countries = dict()
        for name, kind_data in per_country.items():
            try:
                pop = populations[name]
            except:
                pop = 0
            self.countries[name] = Country(name, pop, kind_data)

    def country(self, country_name):
        return self.countries[country_name]

def log(lst):
    return [None if x == 0 else math.log10(x) for x in lst]

db = DB()

to_plot = ['Croatia', 'Switzerland', 'US', 'Italy', 'Spain', 'Germany', 'France']
fig, axes = plt.subplots(3, 1)

for i, series in enumerate(['confirmed', 'recovered', 'dead']):
    ax = axes[i];
    for cname in to_plot:
        ax.plot(db.dates, log(db.country(cname).dispatch(series)), label=cname)
    ax.set_ylabel('# {} permille (log)'.format(series))
    ax.set_xlabel('Date')
    ax.legend()

plt.show()
