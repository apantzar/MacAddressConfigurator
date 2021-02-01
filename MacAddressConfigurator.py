# !/usr/bin/env python
import subprocess
#from random import random
#from randmac import RandMac


class color:
    BLUE = '\033[96m'
    DEFAULT = '\033[0m'
    RED = '\033[91m'




okStr = "---------------------------------------[OK]---------------------------------------"
def checkForUpdates():
    print(color.BLUE + "Installing/Updating net-tools..." + color.DEFAULT)
    subprocess.call(" apt install net-tools", shell=True);
    print(okStr)

    print(color.BLUE + "Installing/Updating python3-pip..." + color.DEFAULT)
    subprocess.call("apt update", shell=True);
    subprocess.call("sudo apt install python3-pip", shell=True);
    from random import random
    
    
    print(okStr)

    print(color.BLUE + "Installing/Updating randmac..." + color.DEFAULT)
    subprocess.call("sudo pip install randmac", shell=True);
    from randmac import RandMac
    difMac = str(RandMac())
    print(okStr)



checkForUpdates()

subprocess.call("ifconfig", shell=True)

interface = input(color.BLUE+"Give the interface you want to configure: "+color.DEFAULT)

subprocess.call("ifconfig " + interface + " down", shell=True)
newMac = input(color.BLUE + "Give new MAC or press (d) for default: " + color.DEFAULT)

if newMac == "d" or "D":

    subprocess.call("sudo ifconfig " + interface + " hw ether " + difMac, shell=True)
else:
    difMac = newMac
    subprocess.call("sudo ifconfig " + interface + " hw ether " + difMac, shell=True)

subprocess.call("sudo ifconfig " + interface + " up", shell=True)

print("")

print(color.RED+"\t\tNew MAC\t\t\n------------------------------------ "+color.DEFAULT)
print(difMac+ "\t\t")
print(color.RED+"------------------------------------"+color.DEFAULT)
print("\n")
print(color.BLUE +"Running 'ifconfig for you'..."+color.DEFAULT)
subprocess.call("sudo ifconfig", shell=True)
subprocess.call("sudo ifconfig " + interface + " up", shell=True)


