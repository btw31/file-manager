import os
import time
from datetime import datetime

REPORT_FILE = "/home/pi/python_ping/report"

def f_size(path):
    if os.path.exists(REPORT_FILE):
        with open(path) as f:
            f.seek(0, os.SEEK_END)
            return f.tell()

while(1):
    size = f_size(REPORT_FILE)
    if size > 100000000:
        if os.path.exists(REPORT_FILE): os.remove(REPORT_FILE)
        with open(REPORT_FILE, "a") as f:
            now = datetime.now()
            cur_time =  now.strftime("%Y%m%d %H%M%S")
            f.write(cur_time + ": File rolled over\n")
    time.sleep(180)
