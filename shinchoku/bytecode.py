#!/usr/bin/env python3
#!cording=utf-8

import sys
import binascii

def c_conv(testfile):
    with open(testfile,"rb") as file:
        chunk = 0
        while chunk !=b'':
            chunk = file.read(1024)
    return chunk

if __main__ == '__main__':
    test = sys.argv[1]
    print(c_conv(test))
