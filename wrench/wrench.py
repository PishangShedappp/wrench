import sys
import argparse

from runner.basicnuclei import bnrunner
from runner.subdomainenumeration import serunner

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
    parser.add_argument('-l', '--list')
    parser.add_argument('-ns', '--nuclei-severity')
    parser.add_argument('-o', '--output')
    parser.add_argument('-esf', '--exclude_subfinder', default=False, action='store_true')
    parser.add_argument('-eaf', '--exclude_assetfinder', default=False, action='store_true')
    parser.add_argument('-eam', '--exclude_amass', default=False, action='store_true')
    return parser.parse_args()

def main(type, domain, list, ns, output, esf ,eaf, eam):
    if type == 'help' or type == 'h':
        print("OPTIONS:")
        print("  h, help                show this help message and exit")
        print(" ")
        print("BASIC SCAN:")
        print("  bn, basicnuclei        run basic nuclei scanning")
        print("     -d, --domain string                target domain to scan")
        print("     -l, --list string                  path to file containing target domain to scan")
        print("     -ns, --nuclei_severity value[]     display output based on severity. [info, low, medium, high, critical, unknown]")
        print("     -o, --output string                output file to write found issues/vulnerabilities")
        print("     -nt, --nuclei_template string[]    list of template or template directory to run(comma-seperated, file)")
        print(" ")
        print("  se, subdomainenumeration        run subdomain enumeration from various tools")
        print("     -d, --domain string                target domain to scan")
        print("     -o, --output string                output file to write found issues/vulnerabilities")
        print("     -esf, --exclude_subfinder          exclude subfinder to run")
        print("     -eaf, --exclude_assetfinder        exclude assetfinder to run")
        print("     -eam, --exclude_amass              exclude amass to run")
        print(" ")

    elif type == 'bn' or type == 'basicnuclei':
        bnrunner(domain, list, ns, output)

    elif type == 'se' or type == 'subdomainenumeration':
        serunner(domain, output, esf, eaf, eam)

    elif type == 'a' or type == 'all':
        print("Scanning all")

def runner():
    args = parse_args()
    type = args.type
    domain = args.domain
    list = args.list
    ns = args.nuclei_severity
    output = args.output
    esf = args.exclude_subfinder
    eaf = args.exclude_assetfinder
    eam = args.exclude_amass
    banner()
    res = main(type, domain, list, ns, output, esf, eaf, eam)

if __name__ == "__main__":
    runner()