#!/usr/bin/env python3
#!cording=utf-8

"""
Get information as available your devices
Tested on iOS 11.4.1(with Jailbreak)
Author: yotti
"""

import frida
import sys

def on_message(message, data):
    try:
        if message:
            print("[log] {0}".format(message["payload"]))
    except Exception as e:
        print(message)
        print(e)

def hook():
    get_available_information ="""
    console.log("[*]Start..");
    if(ObjC.available) {
        send("frida is available");
    } else {
        console.log("frida is not available on your devices");
    }
    console.log("[*]End");
    """

    return get_available_information

if __name__ == '__main__' :
    PACKAGE_NAME = "JailbreakDetection_Objective-C"
    try :
        
        session = frida.get_usb_device().attach(PACKAGE_NAME)
        print ("[log] devices info : {}".format(frida.get_device_manager().enumerate_devices()))
        script = session.create_script(hook())
        script.on('message', on_message)
        script.load()
        sys.stdin.read()
    except KeyboardInterrupt:
        sys.exit(0)
