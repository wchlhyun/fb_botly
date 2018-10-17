import os
currDirectory = os.path.dirname(os.path.abspath(__file__))
import sys
sys.path.append(currDirectory)
import time


import testing as t

headless = False
driver = t.log_in(headless)
seen_messages = set()

while(True):
    seen_messages = t.check(driver, seen_messages)
    print(".")
    time.sleep(1)
