#!/usr/bin/env/python
import argparse
from hashlib import md5

def main():
    if args.infile:
        hash_it(args.infile)

def hash_it(in_file):
    with open(in_file, mode='rb') as content:
        for line in content:
            print(md5(line.rstrip()).hexdigest()[-3:] + ': ' + line.decode('utf-8').rstrip())
        print('\nFull md5 hash of: ' + in_file + ' - ' + md5(open(in_file, 'rb').read()).hexdigest())

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple little code checkr')
    parser.add_argument('-i', '--infile', required=True, help='input file to do hashy things with')
    args = parser.parse_args()
    main()