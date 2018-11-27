# Application analyze by using frida

## prepare

[For mobile device]<br>
wget https://build.frida.re/frida/android/arm/bin/frida-server<br>
adb push frida-server /data/local/tmp<br>
root@JP20835:/data/local/tmp # chmod 700 frida-server<br>
root@JP20835:/data/local/tmp # ./frida-server <br>

[For PC]<br>
$adb forward tcp:27042 tcp:27042<br>
$adb forward tcp:27043 tcp:27043<br>


## program using python