#!/usr/bin/env python3
#!cording=utf-8

"""
Get classes and method
Tested on iOS 11.4.1(With Jailbreak)
Author:yotti(kusama yoshiki)
"""

import sys
import frida
get_method_information = """
console.log("[*] Started: Find Methods")
if (ObjC.available)
{
    for (var className in ObjC.classes)
    {
        if (ObjC.classes.hasOwnProperty(className))
        {
            console.log("[+] Class: " + className);
            var methods = ObjC.classes[className].$ownMethods;
            for (var i = 0; i < methods.length; i++)
            {
                console.log("\t[-] Method: "+methods[i]);
            }
        }
    }
}
else
{
    console.log("Objective-C Runtime is not available!");
}
console.log("[*] Completed: Find Methods")
"""

session = frida.get_usb_device().attach('JailbreakDetection')
script = session.create_script(get_method_information)
print("[*]start scan")
script.load()
print("[*]end scan")
sys.stdin.read()
script.exit()
