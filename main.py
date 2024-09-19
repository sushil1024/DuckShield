from infi.devicemanager import DeviceManager
import time
from block_keystrokes import block
from multiprocessing import Process
from mailto import sendmail
import os
import cv2

default_cnt = 0


def del_logs():
    """
    Delete previous Logs and Images.
    :return: NA
    """
    if os.path.exists("logs/key_log.txt"):
        os.remove("logs/key_log.txt")
    if os.path.exists("camshots/webcam_shot.jpg"):
        os.remove("camshots/webcam_shot.jpg")


def make_dir():
    """
    Creates directory for logs and images.
    :return:
    """
    if not os.path.exists("logs/"):
        os.mkdir('logs')
    if not os.path.exists('camshots/'):
        os.mkdir('camshots')


def check_device():
    """
    Determine no. of default keyboard devices present in the system.
    :return:
    """
    global default_cnt
    dump = []

    dm = DeviceManager()
    dm.root.rescan()

    [dump.append(str(i)) for i in dm.all_devices]

    # count denotes number of devices posing as a keyboard
    for i in dump:
        if "keyboard" in i.lower():
            default_cnt = default_cnt + 1

    print(f"{default_cnt} keyboards detected in device")


def delayed_sendmail(email: str, d_time: int):
    """
    Capture webcam image & send email after 15 seconds delay.
    :param email: str
    :param d_time: int
    :return:
    """
    cap = cv2.VideoCapture(0)       # webcam open
    if cap.isOpened():
        ret, frame = cap.read()
        if ret:
            img_path = os.path.join('camshots', 'webcam_shot.jpg')
            cv2.imwrite(img_path, frame)
            print('Image saved')
        else:
            print('Image not saved')
    else:
        print('Cannot access webcam')
    cap.release()               # release webcam
    cv2.destroyAllWindows()     # close all cv2 processes

    time.sleep(d_time)
    sendmail(email)


def start_process(email_id: str):
    """
    Compare no. of default devices in realtime with updated devices.
    If not matched, block the key events and send alert email.
    :param email_id: str
    :return:
    """
    global default_cnt
    actual_cnt = 0
    dump = []

    dm = DeviceManager()
    dm.root.rescan()

    [dump.append(str(i)) for i in dm.all_devices]

    # count denotes number of devices posing as a keyboard
    for i in dump:
        if "keyboard" in i.lower():
            actual_cnt = actual_cnt + 1
            if actual_cnt > default_cnt:
                print("Unauthorized HID Device Detected! Keyboard Blocked!")

                p1 = Process(target=block)
                p1.start()

                p2 = Process(target=delayed_sendmail, args=(email_id, 15))
                p2.start()

                p1.join()
                p2.join()

                return False

            else:
                print("...")
                time.sleep(0.5)

    return True


if __name__ == '__main__':
    del_logs()
    make_dir()

    email = str(input('Enter admin email ID: '))
    check_device()

    while True:
        flag = start_process(email_id=email)
        if not flag:
            break

    print('Terminating the program')
