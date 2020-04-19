git add .
git commit -m "Automate updates."
git push origin master
git checkout gh-pages
git merge master
git push origin gh-pages
git checkout master
Pause
