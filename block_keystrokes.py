import keyboard
import time
from detect_keys import starting


def block():
    [keyboard.block_key(i) for i in range(150)]

    while True:
        time.sleep(True)
        res = starting()
        if not res:
            break


if __name__ == '__main__':
    block()
