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
if (ObjC.available){
    try{
        var className = "ViewController";
        var methods = (ObjC.classes[className].$onwMethods);
        for (var i = 0; i < methods.length; i++){
            try{
            console.log("[-] "+methods[i]);
            }
            catch(err){
                console.log("[!] Exception1: " + err.message);
                }
            }
        }
    catch(err)
    {
        console.log("[!] Exception2: " + err.message);
        }
}
else
{
    console.log("Objective-C Runtime is not available!");
    }

console.log("[*] Completed: Find Methods")
"""

session = frida.get_usb_device().attach('DVIA-v2')
script = session.create_script(get_method_information)
print("[*]start scan")
script.load()
print("[*]end scan")
sys.stdin.read()
script.exit()
