#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Ping all IP in your network
# It need "netinfo.py" for work, then
# you must use super user powers #
# Author : Dario Lynx
# Edited : Walter Danilo Galante
# Name   : ping_network.py
# Purpose: Ping all IP in your network
# Country: Italy
# Email  : dariolynx@gmail.com
#

# Import user's modules
from .netinfo import NetworkProperties
# Import builtin modules
import os
import ipaddress


__all__ = ["NetworkProperties", "main"]


def main():
    np = NetworkProperties()
    # Returns an iterator over the usable hosts in the network.
    # The usable hosts are all the IP addresses that belong to the network,
    # except the network address itself and the network broadcast address.
    all_hosts = list(ipaddress.IPv4Interface(np.ip_addr + '/' + str(np.cidr)).network.hosts())

    # For each IP address in the subnet, run the ping command
    for i in range(len(all_hosts)):
        # Using os.system instead of subprocess, we obtain easily the return code.
        # Since ping returns 0 if it receives a "pong", and a different value
        # if not, it's easy to guess which hosts are online and which are not.
        # This approach has also the perk of being platform independent, since
        # it's not based on the output of ping on the stdout.
        output = os.system("ping -c 1 -W 1 %s > /dev/null" % str(all_hosts[i]))
        if output == 256:
            print(str(all_hosts[i]), "is Offline -> Destination Host Unreachable")
        elif output == 2:
            print("User interrupted.")
            break
        elif output != 0:
            print(str(all_hosts[i]), "is Offline -> Request timed out. Status: ", output)
        else:
            print(str(all_hosts[i]), "is Online")
            

if __name__ == "__main__":
    main()

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
