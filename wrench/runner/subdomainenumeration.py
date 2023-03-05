import os
import sys
import time

is_windows = sys.platform.startswith("win")

def serunner(domain, output, esf, eaf, eam):
    time.sleep(2)
    # Checking os for clearing terminal
    if is_windows:
        os.system("cls")
    else:
        os.system("clear")

    # Dividing target host
    if domain:
        if output:
            if esf:
                os.system("amass enum -d " + domain + " -o /tmp/amass.out")
                if is_windows:
                    os.system("assetfinder -subs-only " + domain + " > /tmp/assetf.out")
                    os.system("type /tmp/amass.out /tmp/assetf.out > " + output)
                    os.system("rmdir /tmp/")
                else:
                    os.system("assetfinder -subs-only " + domain + " | tee /tmp/assetf.out")
                    os.system("cat /tmp/amass.out /tmp/assetf.out | tee " + output)
                    os.system("rm -r /tmp/")
            elif eaf:
                os.system("subfinder -d " + domain + " -o /tmp/subfinder.out")
                os.system("amass enum -d " + domain + " -o /tmp/amass.out")
                if is_windows:
                    os.system("type /tmp/subfinder.out /tmp/amass.out > " + output)
                    os.system("rmdir /tmp/")
                else:
                    os.system("cat /tmp/subfinder.out /tmp/amass.out | tee " + output)
                    os.system("rm -r /tmp/")
            elif eam:
                os.system("subfinder -d " + domain + " -o /tmp/subfinder.out")
                if is_windows:
                    os.system("assetfinder -subs-only " + domain + " > /tmp/assetf.out")
                    os.system("type /tmp/subfinder.out /tmp/assetf.out > " + output)
                    os.system("rmdir /tmp/")
                else:
                    os.system("assetfinder -subs-only " + domain + " | tee /tmp/assetf.out")
                    os.system("cat /tmp/subfinder.out /tmp/assetf.out | tee " + output)
                    os.system("rm -r /tmp/")
        else:
            if esf:
                os.system("amass enum -d " + domain)
                os.system("assetfinder -subs-only " + domain)
            elif eaf:
                os.system("subfinder -d " + domain)
                os.system("amass enum -d " + domain)    
            elif eam:
                os.system("subfinder -d " + domain)
                os.system("assetfinder -subs-only " + domain)
    else:
        print("[INF] Target needed for scan")