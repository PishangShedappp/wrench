import os
import sys
import time

is_windows = sys.platform.startswith('win')

def bnrunner(domain, list, ns, output):
    time.sleep(2)
    # Checking os for clearing terminal
    if is_windows:
        os.system("cls")
    else:
        os.system("clear")

    # Dividing target host
    if domain:
        if output:
            if ns:
                os.system("nuclei -u " + domain + " -s " + ns + " -o " + output)
            else:
                os.system("nuclei -u " + domain + " -o " + output)
        else:
            if ns:
                os.system("nuclei -u " + domain + " -s " + ns)
            else:
                os.system("nuclei -u " + domain)
    elif list:
        if output:
            if ns:
                os.system("nuclei -l " + list + " -s " + ns + " -o " + output)
            else:
                os.system("nuclei -l " + list + " -o " + output)
        else:
            if ns:
                os.system("nuclei -l " + list + " -s " + ns)
            else:
                os.system("nuclei -l " + list)
    else:
        print("[INF] Target needed for scan")