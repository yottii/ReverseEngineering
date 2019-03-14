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
    hook = """
 if(ObjC.available) {
        var mallocPtr = Module.findExportByName('libsystem_c.dylib', 'malloc');
        var malloc = new NativeFunction(mallocPtr, 'pointer', ['int']);
        Interceptor.replace(mallocPtr, new NativeCallback(function (size) {
        var location = malloc(size)
        send("Allocated " + size + " bytes in " + location);
        return location;
    }, 'pointer', ['int']));

    } else {
        console.log("Objective-C Runtime is not available!");
    }
"""
    return hook

if __name__ == '__main__' :
    PACKAGE_NAME = "JailbreakDetection_Objective-C"
    try :
        
        session = frida.get_usb_device().attach(PACKAGE_NAME)
        #print ("[log] devices info : {}".format(frida.get_device_manager().enumerate_devices()))
        #device = frida.get_device_manager().enumerate_devices()[-1]
        #pid = device.spawn([PACKAGE_NAME])
        #print ("[log] {} is starting. (pid : {})".format(PACKAGE_NAME, pid))
        #session = frida.get_usb_device().attach(PACKAGE_NAME)
        #session = device.attach(pid)
        #device.resume(pid)

        script = session.create_script(do_hook())
        script.on('message', on_message)
        script.load()
        sys.stdin.read()
    except KeyboardInterrupt:
        sys.exit(0)
