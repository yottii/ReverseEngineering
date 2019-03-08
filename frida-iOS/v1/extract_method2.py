#!/usr/bin/env python3
#!cording=utf-8

"""
Get classes and method
Tested on iOS 11.4.1(With Jailbreak)
Author:yotti(kusama yoshiki)
"""

import sys
import frida
import time
get_method_information =  """
console.log("[*] Started: Find Specific Method");
if (ObjC.available)
{
    for (var className in ObjC.classes)
    {
        try
        {
            if (ObjC.classes.hasOwnProperty(className))
            {
                try
                {
                    var methods = eval('ObjC.classes.' + className + '.$methods');
                    for (var i = 0; i < methods.length; i++)
                    {
                        try
                        {
                            //Your function name goes here
                            if(methods[i].includes("Jail"))
                            {
                                console.log("[+] Class: " + className);
                                console.log("\t[-] Method: "+methods[i]);
                            }
                        }
                        catch(err)
                        {
                            console.log("[!] Exception3: " + err.message);
                        }
                    }
                }
                catch(err)
                {
                    console.log("[!] Exception2: " + err.message);
                }
            }
        }
        catch(err)
        {
            console.log("[!] Exception1: " + err.message);
        }
    }
}
else
{
    console.log("Objective-C Runtime is not available!");
}
console.log("[*] Completed: Find Specific Method");
"""

device = frida.get_usb_device(1)
pid = device.spawn("JailbreakDetection")
device.resume(pid)
time.sleep(1) #Without it Java.perform silently fails
session = device.attach(pid)
script = session.create_script(open("s1.js").read())
script.load()
