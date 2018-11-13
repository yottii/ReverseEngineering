#!/usr/bin/env python3
#cording = utf-8

#from pwn import *

import subprocess
import shlex
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

command_line = "diff  {} {}".format(file1, file2)
command_args = shlex.split(command_line)

rc = 0
try:
    rc = subprocess.check_output(command_args)
except subprocess.CalledProcessError as cpe:
    print("shell returncode is not 0.")
    print("returncode: {}".format(cpe.returncode))
    print("output: {}".format(cpe.output))
    rc = cpe.returncode

print(rc)


