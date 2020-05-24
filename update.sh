#!/bin/bash
pipenv run python setup.py py2app -r wallpaper
mv dist/WallpaperChanger.app ~/Desktop
rm -rf build dist
cd ~/Desktop
open -a WallpaperChanger