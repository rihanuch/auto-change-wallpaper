#!/bin/bash
pip3 install pipenv
pipenv install requirements.txt
pipenv run python setup.py py2app -r wallpaper
mv dist/WallpaperChanger.app ~/Desktop
rm -rf build dist
cd ~/Desktop
open -a WallpaperChanger
