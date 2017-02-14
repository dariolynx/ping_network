#!/usr/bin/env python3
# Find local IP, netmask and host's IP
# you must use super user powers #
# Author : Dario Lynx
# Name   : netinfo.py
# Purpose: Find local IP, netmask and host's IP
# Country: Italy
# Email  : dariolynx@gmail.com
#

# Import builtin modules
import itertools
import os
import re

# Check super user privileges
if os.geteuid() != 0:
    if not 'SUDO_UID' in os.environ.keys():
      print("you must use super user powers, try sudo next")
      exit(1)

# Functions

# Get local IP from ifconfig
def get_ip():
    f = os.popen('ifconfig')
    for iface in [' '.join(i) for i in iter(lambda: list(itertools.takewhile(lambda l: not l.isspace(),f)), [])]:
        if re.findall('^(eth|wlan)[0-9]',iface) and re.findall('RUNNING',iface):
            ip = re.findall('(?<=inet\saddr:)[0-9\.]+',iface)
            if ip:
                return ip[0]
            else:
                print("""Warning you are not connected""")
                exit(0)
    return False
# Example
#my_ip = get_ip()
#print("""This is your local IP """)
#print(my_ip)

# Get netmask from ifconfig
def get_netmask():
    f = os.popen('ifconfig')
    for iface in [' '.join(i) for i in iter(lambda: list(itertools.takewhile(lambda l: not l.isspace(),f)), [])]:
        if re.findall('^(eth|wlan)[0-9]',iface) and re.findall('RUNNING',iface):
            nm = re.findall('(?<=Mask:)[0-9\.]+',iface)
            if nm:
                return nm[0]
    return False
# Example
#my_nm = get_netmask()
#print("""This is your netmask """)
#print(my_nm)

# Get broadcast IP froma ifconfig
def get_Bcast():
    f = os.popen('ifconfig')
    for iface in [' '.join(i) for i in iter(lambda: list(itertools.takewhile(lambda l: not l.isspace(),f)), [])]:
        if re.findall('^(eth|wlan)[0-9]',iface) and re.findall('RUNNING',iface):
            Bcast = re.findall('(?<=Bcast:)[0-9\.]+',iface)
            if Bcast:
                return Bcast[0]
    return False
# Example
#my_Bcast = get_Bcast()
#print("""This is your broadcast """)
#print(my_Bcast)

# Get all IP from hostname
ips = os.popen('hostname --all-ip-addresses')
# Example
#my_ips = ips.read()
#print("""Those are your hostname's IPs """)
#print(my_ips)

########################################################################
#netinfo is a python3 software that Find local IP, netmask and host's IP
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
#netinfo  Copyright (C) 2017  Dario Lynx
#This program comes with ABSOLUTELY NO WARRANTY; for details type 'show w'.
#This is free software, and you are welcome to redistribute it
#under certain conditions; type 'show c' for details.
########################################################################
