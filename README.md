# DuckShield
Prevents HID attack/keystroke attack performed by a pre-programmed physical thumb drive ie. Rubber Ducky.

# How it works
1. The software detects and blocks the Rubber Ducky before any severe damage to the system.
2. Alerts the administrator via an email with the log file.
3. The log file contains the registered keystrokes of the Rubber Ducky.
4. The blocked keyboard can be unblocked by pressing a combination of hot keys ie. 'esc + e + m'.

# Instructions
1. Change the sender's email address in the 'mailto.py' file with the organization's email id.
2. The email id to be put into the source code has to have third party access enabled and multi-factor authorization disabled.
3. Change the email id of the Administrator in file 'detect_keys.py'. Replace the 'admin@axample.com' with the Administrator's email ID.
4. You can change the hot keys to unblock the keyboard in the source code.

# Note
1. Press and hold the combination of the keys to unblock the keyboard.
