
#!/usr/bin/env python
import subprocess

class color:
  BLUE = '\033[96m'
  DEFAULT = '\033[0m'

difMac = "02:a0:04:d3:00:11"
okStr = "---------------------------------------[OK]---------------------------------------"


print("Installing/Updating net-tools...")
subprocess.call("sudo apt install net-tools",shell=True);
print(okStr)

subprocess.call("sudo ifconfig",shell=True);

interface=raw_input("Give the interface you want to configure: ")

subprocess.call("sudo ifconfig "+interface+" down",shell=True);
newMac=raw_input(color.BLUE +"Give new MAC or press (d) for default: "+color.DEFAULT)

if(newMac == 'd' or newMac =='D'):
    difMac = newMac
    subprocess.call("sudo ifconfig "+interface+" hw ether " +difMac,shell=True);
else:
    difMac = "02:a0:04:d3:00:11"
    subprocess.call("sudo ifconfig "+interface+" hw ether "+difMac,shell=True)


subprocess.call("sudo ifconfig "+interface+" up",shell=True);

print(okStr)


print("Check new MAC: ")
subprocess.call("sudo ifconfig",shell=True);


