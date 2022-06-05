from infi.devicemanager import DeviceManager
import time
import keyboard
import os


def detect_dev():
    dump = []
    dm = DeviceManager()
    dm.root.rescan()
    devices = dm.all_devices

    for i in devices:
        dump.append(i)

    dump = [str(i) for i in dump]

    count = 0

# count denotes number of devices posing as a keyboard
    for i in dump:
        if "Keyboard" in i:
            count = count + 1
            if count > 1:
                from block_keystrokes import block
                block()

            else:
                print("...")
                time.sleep(1)


if __name__ == '__main__':
    # deletes the previous log file created
    from dellog import delfile
    delfile()
    while True:
        detect_dev()
