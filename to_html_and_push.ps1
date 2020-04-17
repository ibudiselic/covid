jupyter nbconvert analyze.ipynb --to html --output analyze.html
python fix_html.py analyze.html
jupyter nbconvert croatia-nordics-and-some.ipynb --to html --output croatia-nordics-and-some.html
python fix_html.py croatia-nordics-and-some.html
git add .
git commit -m "Add another set of countries; Remove exponential fits from cross-country comparisons; Realign the countries later."
git push origin master
git checkout gh-pages
git merge master
git push origin gh-pages
git checkout master
pause
