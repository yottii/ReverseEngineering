import frida
import sys

session = frida.get_usb_device().attach(2862)
script_string = """
if (ObjC.available)
{
    try
    {
        var className = "JailbreakDetection";
        var funcName = "+ isJailbreak";
        var hook = eval('ObjC.classes.' + className + '["' + funcName + '"]');
        Interceptor.attach(hook.implementation, {
          onEnter: function(args) {
            console.log("param:"+args[0]+" type:"+typeof args[0]);
            send(args[0]);
          },
          onLeave: function(retval) {
            console.log("[*] Class Name: " + className);
            console.log("[*] Method Name: " + funcName);
            console.log("\t[-] Type of return value: " + typeof retval);
            console.log("\t[-] Return Value: " + retval);
            send(retval)
          }
        });
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
"""


script = session.create_script(script_string)


def on_message(message, data):
    if message['type'] == 'error':
        print("[!] " + message['stack'])
    elif message['type'] == 'send':
        print("[i] " + message['payload'])
        addr = int(message['payload'], 16)
        print("try to read addr content...")
        addr_content = session.read_bytes(addr, 4)
        print("addr content:" + addr_content)
    else:
        print(message)


script.on('message', on_message)
script.load()
sys.stdin.read()
