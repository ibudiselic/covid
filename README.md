Simple analysis of Covid data from https://github.com/CSSEGISandData/COVID-19.

If you see this by some chance, please don't read too much into it:

1. I'm not a data analyst - not even close.

2. I'm not an epidemiologist - not even close.

3. I didn't invest much effort into verifying things etc.

I'm making no guarantees on the correctness of any of this. Listen to your local authorities for authoritative information.

There's an interactive sandbox on Binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ibudiselic/covid/master?filepath=binder_sandbox.ipynb)
Binder needs a few minutes to set up the environment before you can start.
This is ineractive both in the sense of being able to edit anything, and having the charts be interactive (e.g. show actual numbers at each point on hover). 
You can also switch to any of the premade notebooks there, or look at lib.ipynb to understand more about the library and try your own analyses.

If you just want to look at the results for some fixed sets of countries, see:
https://ibudiselic.github.io/covid/analyze.html (and there are also links to other analyses at the top).

I usually update the data once per day, morning time in Europe.

The country population data comes from https://www.worldometers.info/world-population/population-by-country/

To run one of the notebooks locally, use:

$ jupyter notebook analyze.ipynb
