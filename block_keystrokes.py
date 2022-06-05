# blocks keyboard until 'esc + e' combination is pressed
import sys

import keyboard
import time


def block():
    for i in range(150):
        keyboard.block_key(i)

    while True:
        time.sleep(True)
        from detect_keys import starting
        starting()
        # if keyboard.is_pressed('Esc') and keyboard.is_pressed('e') and keyboard.is_pressed('m'):
        #     del sys.modules['detect_keys']
        #     break


if __name__ == '__main__':
    block()
