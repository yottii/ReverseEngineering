#!/usr/bin/env python3
#!cording=utf-8

"""
Get classes and method
Tested on iOS 11.4.1(With Jailbreak)
Author:yotti
"""


import sys
import frida

get_classes_information = """
if (ObjC.available){
    for (var className in ObjC.classes){
        if (ObjC.classes.hasOwnProperty(className)){
            console.log(className);
        }
    }
}
else
{
    console.log("This Process is not available..");
}
"""
session = frida.get_usb_device().attach('JailbreakDetection_Objective-C')
script = session.create_script(get_classes_information)
print("[*]start scan")
script.load()
print("[*]end scan")
sys.stdin.read()
script.exit()
