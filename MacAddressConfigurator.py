# !/usr/bin/env python
import subprocess


class color:
    BLUE = '\033[96m'
    DEFAULT = '\033[0m'


difMac = "10:fe:ad:33:4c:65"
okStr = "---------------------------------------[OK]---------------------------------------"

print("Installing/Updating net-tools...")
subprocess.call(" apt install net-tools", shell=True);
print(okStr)

subprocess.call("ifconfig", shell=True)

interface = input("Give the interface you want to configure: ")

subprocess.call("ifconfig " + interface + " down", shell=True)
newMac = input(color.BLUE + "Give new MAC or press (d) for default: " + color.DEFAULT)

if newMac == "d" or "D":

    subprocess.call(" ifconfig " + interface + " hw ether " + difMac, shell=True)
else:
    difMac = newMac
    subprocess.call(" ifconfig " + interface + " hw ether " + difMac, shell=True)

subprocess.call("sudo ifconfig " + interface + " up", shell=True)

print(okStr)

print("Check new MAC: ")
subprocess.call("sudo ifconfig", shell=True)
subprocess.call("sudo ifconfig " + interface + " up", shell=True)


