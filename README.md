# Auto change wallpaper MacOS dark mode
Script to detect change of theme to or from dark mode in MacOS

## Installation
### Basic
This is the basic installation which *does not* auto start on startup
1. Download or clone the repository
2. Open up the console in the downloaded folder
3. Paste the following commands (it may prompt you to put your password)
```sh
chmod +x install.sh update.sh
./install.sh
```
4. The system will ask you if the app can control "Finder", give it the `Ok`
5. Once the install finishes, the application will auto start

### Auto open on startup
You can make the app automatically start on the background so that you don't have to worry with the following steps:
1. Open System Preferences > Users & Groups > Startup
2. Click the lock icon to unlock adding the application on startup
3. Add the application that was automatically created in your desktop

## Usage

The application comes with default photos that I have taken in my journeys (not nearly as clean as they can be). You have the liberty of adding or removing wallpapers for your own personal use!

To add or remove your own pictures, simply do the following
1. Create a folder with any name you want in the `wallpaper` folder
2. In the folder that you created add two `.jpg` (note the picture format) pictures, `light.jpg` and `dark.jpg`, each one corresponding to their respective theme
3. Run the following command in your terminal from the folder which contains the code
```sh
./update.sh
```
4. That's it! You are ready to go!