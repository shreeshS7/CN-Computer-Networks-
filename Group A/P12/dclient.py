

import os
#Install DHCP Package

os.system("sudo dhclient -r wlp2s0")
os.system("sudo dhclient -r -v wlp2s0")
os.system("sudo dhclient -v wlp2s0")
