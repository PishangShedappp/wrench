import os
import sys
import time

is_windows = sys.platform.startswith("win")

def serunner(domain, output):
    time.sleep(2)
    # Checking os for clearing terminal
    if is_windows:
        os.system("cls")
    else:
        os.system("clear")

    # Dividing target host
    if domain:
        if output:
            os.system("subfinder -d " + domain + " -o " + output)
        else:
            os.system("subfinder -d " + domain)
    else:
        print("[INF] Target needed for scan")