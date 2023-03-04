import os
import sys
import time

is_windows = sys.platform.startswith('win')

def bnrunner():
    time.sleep(3)
    if is_windows:
        os.system("cls")
    else:
        os.system("clear")
    os.system("nuclei")