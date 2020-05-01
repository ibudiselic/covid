Invoke-WebRequest -OutFile data/confirmed.csv https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv
Invoke-WebRequest -OutFile data/dead.csv https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv
Invoke-WebRequest -OutFile data/recovered.csv https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv

$fnames = @("analyze", "croatia-nordics-and-some", "europe", "north_america", "asia", "south_america", "africa")

ForEach ($fname in $fnames) {
  jupyter nbconvert --to notebook --inplace --execute "$fname.ipynb"
  jupyter nbconvert "$fname.ipynb" --to html --output "$fname.html"
  jupyter nbconvert --ClearOutputPreprocessor.enabled=True --to notebook --inplace "$fname.ipynb"
}

$htmls = $fnames -replace "$",".html"
python fix_html.py @htmls

Pause
