#!/usr/bin/env bash

# remove all files except these:
shopt -s extglob
rm -rv !(".gitignore"|"CNAME"|".git"|".nojekyll"|".venv"|".vscode"|"deploy.sh"|"src"|"requirements.txt"| "README.md"|"node_modules"|"localhost:8000")
shopt -u extglob

# move files from site directory
mv localhost:8000/* .

# remove unneeded directory
rm -rfv localhost:8000

# add files to git
git add .

# commit site update
COMMIT=$(git rev-parse --short HEAD)
git commit -m "Deployed ${COMMIT}; Updated website"

# push changes
git push -u origin gh-pages

