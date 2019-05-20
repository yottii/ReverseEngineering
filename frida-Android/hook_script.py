import frida
import sys

package_name = "owasp.mstg.uncrackable1"

def on_message(message,data):
    print(message)

hooking = """
setImmediate(function(){
        console.log("[*]START");
        Java.perform(function(){
                console.log("[*]system.exit(0); is invalid");
                var exitClass = Java.use("java.lang.System");
                exitClass.exit.implementation = function(){
                    console.log("[*]system called");
                    }
                })
        });
"""

process = frida.get_usb_device().attach(package_name)
script = process.create_script(hooking)
script.on("message",on_message)
print("[*]scpipt load")
script.load()
sys.stdin.read()
