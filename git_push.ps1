git add .
git commit -m "Add requirements.txt for Binder."
git push origin master
git checkout gh-pages
git merge master
git push origin gh-pages
git checkout master
Pause
