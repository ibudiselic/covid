# Simple analysis of Covid data from https://github.com/CSSEGISandData/COVID-19.

## Disclaimer

If you see this by some chance, please don't read too much into it:

1. I'm not a data analyst - not even close.

2. I'm not an epidemiologist - not even close.

3. I didn't invest much effort into verifying things etc.

I'm making no guarantees on the correctness of any of this. Listen to your local authorities for authoritative information.

## Usage

### Interactive usage

There's an interactive sandbox on Binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ibudiselic/covid/master?filepath=binder_sandbox.ipynb)

Binder needs a few minutes to set up the environment before you can start.
This is ineractive both in the sense of being able to edit anything, and having the charts be interactive (e.g. show actual numbers at each point on hover). 
You can also switch to any of the premade notebooks there, or look at lib.ipynb to understand more about the library and try your own analyses.

### See pre-generated analyses

If you just want to look at the results for some fixed sets of countries, see https://ibudiselic.github.io/covid/analyze.html (and there are also links to other analyses at the top).

### Run locally

Running this locally requires Python3. Install the dependencies using:

$ pip install -r requirements_for_update_and_regenerate_data.txt

or similar (e.g. create a virtual environment). YMMV - e.g. on Windows, you may need to install some MSVC tools which are needed to build some of the libraries.

To run a notebook, use:

$ jupyter notebook analyze.ipynb

## Other information

I created this in the first weeks of the Covid pandemic. I've since removed/disabled some of the features that don't work anymore like curve fitting, and am using this to occasionally get an update on the numbers.

The country population data comes from https://www.worldometers.info/world-population/population-by-country/
