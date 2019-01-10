#!/usr/bin/env python3
#!cording:utf-8

import sys
import hashlib

strings = sys.argv[1]

def cal_hash(string):
    hash = hashlib.sha256(b'screen.png').hexdigest()
    return hash


test = cal_hash(strings)
print(test)
