jupyter nbconvert analyze.ipynb --to html --output analyze.html
python fix_html.py
git add .
git commit -m "Remove stray data."
git push origin master
git checkout gh-pages
git merge master
git push origin gh-pages
git checkout master
pause
