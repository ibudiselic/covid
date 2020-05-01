git add .
git commit -m "Set up Binder and add a Binder sandbox. Also more impl. consolidation."
git push origin master
git checkout gh-pages
git merge master
git push origin gh-pages
git checkout master
Pause
