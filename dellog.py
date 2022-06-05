import os


# deletes the previous log file created
def delfile():
    if os.path.exists("logs/key_log.txt"):
        os.remove("logs/key_log.txt")
