#/usr/bin/env python3
#!cording=utf-8

"""
Get classes and method
Tested on iOS 11.4.1(With Jailbreak)
Author:yotti(kusama yoshiki)
"""


import sys
import frida

get_method_information = """
if (ObjC.available) { 
    try { 
        var className = "JailbreakDetectionVC"; 
        var funcName = "- isJailbroken"; 
        var hook = eval('ObjC.classes.' + className + '["' + funcName + '"]');
        
        Interceptor.attach(hook.implementation, { 
                
                onLeave: function(retval) { 
                    console.log("[*] Class Name: " + className);
                    console.log("[*] Method Name: " + funcName); 
                    console.log("\t[-] Type of return value: " + typeof retval);
                    console.log("\t[-] Return Value: " + retval); 
                    } 
                }); 
        } 
    catch(err) { 
        console.log("[!] Exception2: " + err.message); 
        }
    } 
else{ 
    console.log("Objective-C Runtime is not available!"); 
    }

"""



session = frida.get_usb_device().attach('DVIA-v2')
script = session.create_script(get_method_information)
print("[*]start scan")
script.load()
print("[*]end scan")
sys.stdin.read()
script.exit()
