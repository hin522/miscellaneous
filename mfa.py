#!/usr/bin/env python3

import pyotp
import getopt
import sys, os

secret = {
    'mgt': '<secret>',
    'dev1': '<secret>'
}

def usage():
    print('Usage:')
    print('  '+os.path.basename(__file__),'-k <key_name>')
    print('  '+os.path.basename(__file__),'(-h | --help)')
    print()
    print('Options:')
    print('  -k, --key <key_name>   Use this key to generate OTP.')
    print('  -h, --help             Show this help.')

def getopts(argv):
    key = ''
    try:
        opts, args = getopt.getopt(argv,'k:',['key='])
    except getopt.GetoptError:
        usage()
        sys.exit(1)
    for opt, arg in opts:
        if opt in ('-k','--key'):
            key = arg
    if not key:
        key = 'mgt'
        #print('Error: Missing arguments')
        #usage()
        #sys.exit(1)
    return key

def main():
    key = getopts(sys.argv[1:])
    totp = pyotp.totp.TOTP(secret[key])
    print(key)
    print(totp.now())

if __name__ == '__main__':
    main()
