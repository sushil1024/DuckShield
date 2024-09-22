from infi.devicemanager import DeviceManager
import time
# from block_keystrokes import block
from multiprocessing import Process
# from mailto import sendmail
import os
import cv2
# from detect_keys import starting
import keyboard
from pynput.keyboard import Listener
import logging
import yagmail
from dotenv import load_dotenv, set_key
from pathlib import Path

env_path = Path('.env')

default_cnt = 0


class Helper:
    def del_logs(self):
        """
        Delete previous Logs and Images.
        :return: NA
        """
        if os.path.exists("logs/key_log.txt"):
            os.remove("logs/key_log.txt")
        if os.path.exists("camshots/webcam_shot.jpg"):
            os.remove("camshots/webcam_shot.jpg")

    def make_dir(self):
        """
        Creates directory for logs and images.
        :return:
        """
        if not os.path.exists("logs/"):
            os.mkdir('logs')
        if not os.path.exists('camshots/'):
            os.mkdir('camshots')

    def check_device(self):
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
                default_cnt += 1

        print(f"{default_cnt} keyboards detected in device")

    def _sendmail(self, a_email: str, s_email: str, s_password: str):
        """
        Send email with attachments.
        :return:
        """
        # credentials of sender
        yag = yagmail.SMTP(user=s_email, password=s_password)

        # details of the email
        yag.send(
            to=a_email,
            subject="SECURITY BREACH DETECTED",
            contents=f"HID attack detected for user: {os.getlogin()} \nPlease refer the attached webcam capture & logs "
                     f"for investigation.",
            attachments=["logs/key_log.txt", "camshots/webcam_shot.jpg"],
        )

        print(f"Email sent")

    def keys_block(self):
        """
        Block keystrokes + call function to log keystrokes.
        :return:
        """
        [keyboard.block_key(i) for i in range(150)]

        while True:
            time.sleep(True)
            res = self.key_log()
            if not res:
                break

    def key_log(self):
        """
        Key logger + condition to break the keystroke block.
        :return: bool
        """
        if not os.path.exists(os.getcwd() + '/logs/'):
            os.mkdir('logs')

        log_directory = os.getcwd() + '/logs/'  # where to save the file
        logging.basicConfig(filename=(log_directory + "key_log.txt"), level=logging.DEBUG,
                            format='%(asctime)s: %(message)s')

        # function in logging
        def on_press(key):
            logging.info(key)
            if keyboard.is_pressed('Esc') and keyboard.is_pressed('e') and keyboard.is_pressed('m'):
                exit()

        with Listener(on_press=on_press) as listener:
            listener.join()  # infinite cycle

        return False


class DuckShield(Helper):
    def __init__(self):
        self.del_logs()
        self.make_dir()
        self.admin_email = str(input('Enter admin email ID: '))

        if env_path.exists():
            print('env found')
            load_dotenv()

            self.sender_email = os.getenv('EMAIL_ID')
            self.sender_password = os.getenv('PASSWORD')

        else:
            print('env not found')
            self.sender_email = str(input("Enter sender's email: "))
            self.sender_password = str(input("Enter sender's password: "))

            set_key(dotenv_path=env_path, key_to_set='EMAIL_ID', value_to_set=self.sender_email)
            set_key(dotenv_path=env_path, key_to_set='PASSWORD', value_to_set=self.sender_password)

        self.check_device()

    def delayed_sendmail(self, admin_email: str, d_time: int = 15):
        """
        Capture webcam image & send email after 15 seconds delay.
        :param admin_email:
        :param d_time: int
        :return:
        """
        cap = cv2.VideoCapture(0)       # webcam open
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                img_path = os.path.join('camshots', 'webcam_shot.jpg')
                cv2.imwrite(img_path, frame)
                print('Image captured')
            else:
                print('Image not captured')
        else:
            print('Cannot access webcam')
        cap.release()                   # release webcam
        cv2.destroyAllWindows()         # close all cv2 processes

        time.sleep(d_time)
        self._sendmail(a_email=admin_email, s_email=self.sender_email, s_password=self.sender_password)

    def start_process(self):
        """
        Compare no. of default devices in realtime with updated devices.
        If not matched, block the key events and send alert email.
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

        if actual_cnt != default_cnt:
            print("Unauthorized HID Device Detected! Keyboard Blocked!")

            p1 = Process(target=self.keys_block)
            p1.start()

            p2 = Process(target=self.delayed_sendmail, args=(self.admin_email, 5))
            p2.start()

            p1.join()
            p2.join()

            return False

        else:
            print("...")
            time.sleep(0.5)

        return True


if __name__ == '__main__':
    obj = DuckShield()

    while True:
        if not obj.start_process():
            break

    print('Terminating the program')

    input()
