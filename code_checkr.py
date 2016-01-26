#!/usr/bin/env/python
import argparse
from hashlib import md5

def main():
    if args.file:
        hash_it(args.file)

def hash_it(file_name):
    with open(file_name, mode='rb') as content:
        for line in content:
            print(md5(line).hexdigest()[-3:] + ': ' + line.decode('utf-8').strip('\n'))
        print('\nFull md5 hash of: ' + file_name + ' - ' + md5(open(file_name, 'rb').read()).hexdigest())

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple little code checkr')
    parser.add_argument('-f', '--file', required=True, help='file to do hashy things with')
    args = parser.parse_args()
    print(args.file)
    main()