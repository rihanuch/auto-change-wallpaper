import os
import threading
import time
import logging
import random


def is_dark():
    return os.system('defaults read -g AppleInterfaceStyle &>/dev/null') == 0

def color_scheme_system():
    if is_dark() == True:
        return 'dark'
    return 'light'

def change_wallpaper(path):
    color_scheme = {
        'light': os.path.abspath(f'{path}/light.jpg'),
        'dark': os.path.abspath(f'{path}/dark.jpg')
    }
    cmd = f"""osascript -e 'tell application "Finder" to set desktop picture to POSIX file "{color_scheme[color_scheme_system()]}"'"""
    os.system(cmd)

def change_background_listener(name, path):
    current_scheme = color_scheme_system()

    logging.info(f'Thread {name}: starting')
    # on start thread change to the prefered configuration
    # with a random selection of files
    logging.info(f'Thread {name}: checking color scheme and setting accordingly ({current_scheme})')
    change_wallpaper(path)

    while True:
        if current_scheme != color_scheme_system():
            current_scheme = color_scheme_system()
            logging.info(f'Thread {name}: changing wallpaper to {current_scheme}')
            change_wallpaper(path)
        time.sleep(1)



if __name__ == '__main__':
    # randomize the pair of pictures
    random_folder = random.choice([os.path.abspath('wallpaper/' + folder) for folder in os.listdir('wallpaper/')])
    logging.basicConfig(format='%(asctime)s: %(message)s', level=logging.INFO, datefmt='%H:%M:%S')
    logging.info('Starting color scheme listener and wallpaper changer')
    wallpaper_changer = threading.Thread(target=change_background_listener, args=('wallpaper changer', random_folder, ))
    wallpaper_changer.start()