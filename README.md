# Anti-Rubber-Ducky
Prevents HID attack/Keystroke attack performed by physical thumb drives known as Rubber Ducky.

# How it works
1. This software detects and blocks the Rubber Ducky before any severe damage to the system.
2. It alerts the administrator of the computer that security breach has taken place at the office by sending the admin an email with a 'log.txt' file.
3. The log file contains the intentions of the Rubber Ducky like what it was trying to access and what keystrokes were pressed.
4. The blocked keyboard can be unblocked by pressing a combination of hot keys.

# Instructions
1. Change the sender's email address in the 'mailto.py' file with the organization's email id.
2. The email id to be put into the source code has to have third party access enabled and multi-factor authorization disabled.
3. Change the email id of the Administrator in file 'detect_keys.py'. Replace the 'admin@axample.com' with the Administrator's email ID.
4. You can change the hot keys to unblock the keyboard in the source code.

# Requirements
infi.devicemanager==0.2.22
keyboard==0.13.5
pynput==1.7.5
logging==0.4.9.6

# Future Scope
This project has future scope of adding many more handful features.
