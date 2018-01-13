# PiDisplaySleep

A powersaver code written in python3 to put your Pi's display to sleep when you are not near it (checks if your phone is connected to the wifi !). This code is mainly aimed to run on smart mirrors(I use MagicMirror). If you live in a dorm room like me and dont want your mirror up all day long when you are away: this does the purpose !

Set up :
  Enter your phone's or whatever devices' IP address in the script.
  Run the script at boot OR just run the main.py as : " python main.py & " through ssh and exit ssh with Ctrl + D. This will     run the script in background until the next power down.

Note: this project uses the nmap package to do network scans; make sure you install it on your device using 
$ sudo apt-get install nmap
