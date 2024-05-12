""" The code is developed for Educational Purpose Only , learn and hack yourself
                      --> BY HACK WITH ROHIT TAMIL"""

import subprocess 
import pyfiglet 

msg = pyfiglet.figlet_format("MAC spoofing is a Home Address !!!!")
print(msg)
n=input("Enter your Network interface eth0 or wlan0 : ")
i=input("Enter New Home Address to Fast Spoof : ")
subprocess.call(["ifconfig",n,"down"])
subprocess.call(["ifconfig",n,"hw","ether",i])
subprocess.call(["ifconfig",n","up"])

print("Home address changed Successfully!!!")

