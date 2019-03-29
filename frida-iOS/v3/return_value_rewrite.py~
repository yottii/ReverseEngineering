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
    return_value_rewrite = """
    if(ObjC.available) {
        var class_checker = ObjC.classes.JailbreakDetection;
        var methods_checker = class_checker.$ownMethods;
        var isApplication = class_checker['+ isJailbreak'];

        Interceptor.attach(isApplication.implementation, {
                onEnter: function(args) {
                    var target = new ObjC.Object(args[0]);
                    var sel = ObjC.selectorAsString(args[1]);
                    send("Target class : " + target.$className);
                    send("Target selector : " + sel);
                    },
                onLeave: function(retVal) {
                    send("Old return : " + retVal);
                    retVal.replace("0");
                    send("New return : " + retVal);
                    }
                });
        } else {
        console.log("frida is not available on your devices");
        }
"""
    return return_value_rewrite

if __name__ == '__main__' :
    PACKAGE_NAME = "JailbreakDetection_Objective-C"
    try :
        
        session = frida.get_usb_device().attach(PACKAGE_NAME)
        script = session.create_script(hook())
        script.on('message', on_message)
        script.load()
        sys.stdin.read()
    except KeyboardInterrupt:
        sys.exit(0)
