#!/usr/bin/env python3

from struct import *                                                            
import sys
import binascii
f = open(sys.argv[1],"rb")

def hex_convert(string):
    i = 0
    save = ''
    while (i < 1000):
        c = string.read(1)
        if not c: break
        save = ''.join(unpack("B",c))
    f.close()
    return save

test = hex_convert(f)

print(test)

