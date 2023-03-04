import sys
import argparse

from runner.basicnuclei import bnrunner

is_windows = sys.platform.startswith('win')

def banner():
    print("""
                 _____                _____
                /___  \______________/  ___\ 
                    \                  /
                ____/  ______________  \____
                \_____/              \_____/  Wrench
    """)
    print("[INF] Have problems? Create issues at 'https://github.com/PishangShedappp/wrench/issues'")
    print(" ")

class MyArgumentParser(argparse.ArgumentParser):

    def print_help(self, file=None):
        banner()
        if file is None:
            file = sys.stdout
        OPTIONS = "OPTIONS:"
        options1 = "  -h, --help            show this help message and exit"
        options2 = "  -t, --type            type of runner you want to run OR `-t help` to learn more"
        blank = " "
        file.write(OPTIONS + "\n")
        file.write(options1 + "\n")
        file.write(options2 + "\n")
        file.write(blank)

def parser_error(errmsg):
    banner()
    if is_windows:
        print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
        print("Error: " + errmsg)
    else:
        print("Usage: python3 " + sys.argv[0] + " [Options] use -h for help")
        print("Error: " + errmsg)
    sys.exit()

def parse_args():
    if is_windows:
        #parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -t type")
        parser=MyArgumentParser()
    else:
        parser = argparse.ArgumentParser(epilog='\tExample: \r\npython3 ' + sys.argv[0] + " -t type")
    parser.error = parser_error
    parser.add_argument('-t', '--type', required=True)
    parser.add_argument('-d', '--domain')
    return parser.parse_args()

def main(type):
    if type == 'help' or type == 'h':
        print("OPTIONS:")
        print("  h, help                show this help message and exit")
        print(" ")
        print("BASIC SCAN:")
        print("  bn, basicnuclei        run basic nuclei scanning")
        print("     -d, --domain string            target domain to scan")

    elif type == 'bn' or type == 'basicnuclei':
        bnrunner()

def runner():
    args = parse_args()
    type = args.type
    domain = args.domain
    banner()
    res = main(type)

if __name__ == "__main__":
    runner()