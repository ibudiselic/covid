git add .
git commit -m "Clear notebook outputs after generating HTML reports."
git push origin master
git checkout gh-pages
git merge master
git push origin gh-pages
git checkout master
Pause
