#!/usr/bin/env python3

from collections import Counter
import collections
import sys
import pylab as plt
from numpy import *


def hex_conv(test):
    yo = test.encode("utf-8")
    te = yo.hex()
    li = [(i+j) for (i,j) in zip(te[::2],te[1::2])]
    return li

test = sys.argv[1]
f = open(test,"r")
sum=''
for row in f:
    sum+=row

a = collections.Counter(hex_conv(sum))
x = list(a.keys())
y = list(a.values())

plt.plot(x,y)
plt.show()
