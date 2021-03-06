#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Date:2018-11-18
#file: test python module sys

import sys
def readfile(filename):
    '''Print a file to the standard output'''
    f = open(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line,)
    f.close()
if len(sys.argv) < 2:
    print('No action apecified')
    sys.exit()
if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    if  option == 'version':
        print('Version 1.2')
    elif option == 'help':
        print(''' \
        This program print files to the standard output.
        --version: Print the version number
        --help: Display this help''')
    else:
        print('Unknown print')
else:
    for filename in sys.argv[1:]:
        readfile(filename)