#!/usr/bin/env python3
# Ping all IP in your network
# It need "netinfo.py" for work, then
# you must use super user powers #
# Author : Dario Lynx
# Name   : ping_network.py
# Purpose: Ping all IP in your network
# Country: Italy
# Email  : dariolynx@gmail.com
#

# Import user's modules
from netinfo import *
# Import builtin modules
import subprocess
import ipaddress

# Returns an iterator over the usable hosts in the network.
# The usable hosts are all the IP addresses that belong to the network,
# except the network address itself and the network broadcast address.
all_hosts = list(ipaddress.IPv4Interface(get_ip() + '/' + get_netmask()).network.hosts())

# For each IP address in the subnet, run the ping command
for i in range(len(all_hosts)):
    output = subprocess.Popen(['ping', '-c', '1', '-W 10', str(all_hosts[i])], stdout=subprocess.PIPE).communicate()[0]
    if "Destination Host Unreachable" in output.decode('utf-8'):
        pass
#        print(str(all_hosts[i]), "is Offline -> Destination Host Unreachable")
    elif "Request timed out" in output.decode('utf-8'):
        print(str(all_hosts[i]), "is Offline -> Request timed out")
    else:
        print(str(all_hosts[i]), "is Online")

########################################################################
#ping_network is a python3 software that Ping all IP in your network
#Copyright (C) 2017  Dario Lynx

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.
########################################################################
#ping_network  Copyright (C) 2017  Dario Lynx
#This program comes with ABSOLUTELY NO WARRANTY; for details type 'show w'.
#This is free software, and you are welcome to redistribute it
#under certain conditions; type 'show c' for details.
########################################################################
