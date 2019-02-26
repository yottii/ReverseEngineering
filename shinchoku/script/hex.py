#!/usr/bin/env python3

import sys

#filename = sys.argv[0]

def hex_convert(file):
    test = ''
    for s in file:
        s = ord(s)
        test += s

        return test

#f1 = open("filename","r") read only
#test = hex_convert(f1)
test = hex_convert("yotti")
print(test)
