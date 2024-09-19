from infi.devicemanager import DeviceManager
import time
import keyboard
import os
from dellog import delfile
from block_keystrokes import block
# from log_config import get_logger, curr_time
# logger = get_logger(__name__)

keyb_count = 0
# exec_time = 30


def checkDevice():
    global keyb_count
    dump = []

    dm = DeviceManager()
    dm.root.rescan()
    devices = dm.all_devices

    for i in devices:
        dump.append(i)

    # dump = [str(i) for i in dump]

    # count denotes number of devices posing as a keyboard
    for i in dump:
        if "keyboard" in str(i).lower():
            keyb_count = keyb_count + 1

    print(f"{keyb_count} keyboards detected in device")


def start_process():
    global keyb_count
    count = 0
    dump = []

    dm = DeviceManager()
    dm.root.rescan()
    devices = dm.all_devices

    for i in devices:
        dump.append(i)

    # count denotes number of devices posing as a keyboard
    for i in dump:
        if "keyboard" in str(i).lower():
            count = count + 1
            if count > keyb_count:
                print("Unauthorized HID Device Detected! Keyboard Blocked!")
                block()

            else:
                print("...")
                time.sleep(1)


if __name__ == '__main__':
    # deletes the previous log file created
    delfile()

    checkDevice()

    start_time = time.time()
    while True:
        start_process()
        # if time.time() - start_time > exec_time:
        #     break
