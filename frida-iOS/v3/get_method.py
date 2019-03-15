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

def do_hook():
    get_method_information = """
    console.log("[*]Start");
    if(ObjC.available) {
        var class_checker = ObjC.classes.JailbreakDetection;
        var methods_checker = class_checker.$ownMethods;
        methods_checker.forEach(function(m) {
                send(m);
                });
        } else {
        console.log("frida is not availabe on your devices");
        }
    console.log("[*]End");
"""
    return get_method_information

if __name__ == '__main__' :
    PACKAGE_NAME = "JailbreakDetection_Objective-C"
    try :
        
        session = frida.get_usb_device().attach(PACKAGE_NAME)
        script = session.create_script(do_hook())
        script.on('message', on_message)
        script.load()
        sys.stdin.read()
    except KeyboardInterrupt:
        sys.exit(0)
