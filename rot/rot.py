#!/usr/bin/env python3
#cording = utf-8


def Caeser(string, shift): # this is caeser program
    save = ''
    for s in string:
        s = ord(s)
        if 65 <= s and s <= 90:
            s = s + shift
            if s > 90
               zurasu = s - 90
               s = 65 + zurasu
        elif 97 <= s and 122 >= s :
            s = s + shift
            if s > 122:
               zura = s - 122
               s = s + zura
        s = chr(s)
        save += s
    return save

f1 = open("./filename1","r") #Designation file 1

for s in
