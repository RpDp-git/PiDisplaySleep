from os import popen,system
from time import sleep
state=1 #State of the display 1 On 0 Off
ip="192.168.1.3" #Enter the IP address of the device that should keep the display awake

while True:
    nmap_out=str(popen('nmap -sP '+ip).read()) #nmap command to scan on the given IP address

    if nmap_out.find('latency') == -1:  #looks for the word "latency" in the output
        if state==0 :                   #this nested if makes sure that commands are not repeated
            pass
        else :
            system('vcgencmd display_power 0')  #Bash command that turns off the display
            state=0                             #Updating the display state variable

    elif nmap_out.find('latency') > 1:
        if state==1:
            pass
        else :
            system('vcgencmd display_power 1') #Bash command to turn on the display
            state=1

    sleep(5) #Scan rate in seconds
