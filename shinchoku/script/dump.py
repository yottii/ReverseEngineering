from struct import *                                                            
import sys
import binascii
f = open(sys.argv[1],"rb")
maxLoop = int(sys.argv[2])
i=0
while (i < maxLoop):
    c = f.read(1)
    if not c: break
    print("%02x " % unpack("B",c), end="")
    if (i % 8) == 7:
        print("")
    i = i + 1
if ((i - 1) % 8) != 7:
    print("")
f.close()

