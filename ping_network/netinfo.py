#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Find local IP, netmask and host's IP
# you must use super user powers #
# Author : Dario Lynx
# Edited : Walter Danilo Galante
# Name   : netinfo.py
# Purpose: Find local IP, netmask and host's IP
# Country: Italy
# Email  : dariolynx@gmail.com
#

# Import builtin modules
import itertools
import os
import re

# Import netifaces library
import netifaces 
# `netifaces` (https://bitbucket.org/al45tair/netifaces) is a library
# that provides almost OS-independent APIs for python to interact 
# with the system networking interfaces. 


class NetworkPropertiesException(Exception):
    """
    Exception class to raise in case something weird happens
    while trying to retrieve the network info.
    """
    pass


class NetworkProperties(object):
    """
    Class used to retrieve and cache the system network interfaces
    information, with an easy to use interface itself.
    The constructor takes the parameter `check_superuser` (True|False)
    to decide whether it should check for superuser privileges
    before attempting to retrieve the network interfaces info from
    the system.

    Example:

    >>> np = NetworkProperties()
    >>> print(np.ip_addr)
    >>> 192.168.1.12
    >>> print(np.gateway)
    >>> 192.168.1.1
    >>> print(np.interface)
    >>> eth0
    >>> print(np.netmask)
    >>> 255.255.255.0
    >>> print(np.broadcast)
    >>> 192.168.1.255
    """    
    def __init__(self, check_superuser=True):
        self.network_info = None
        self.check_superuser = check_superuser
        self.__get_info()

    def __check_superuser(self):
        # Check super user privileges.
        #
        # Raises a NetworkPropertiesException in case 
        # the user doesn't have superuser privileges
        if os.geteuid() != 0:
            if not 'SUDO_UID' in os.environ.keys():
              raise NetworkPropertiesException(
                "You must have superuser powers, please try with `sudo` next time.")
    
    @classmethod
    def calc_cidr(cls, netmask):
        # Method used to calculate the cidr from the netmask
        # address. Sums the number of ones (1) in the binary
        # representation of the netmask address.
        return sum([bin(int(x)).count("1") for x in netmask.split(".")])

    def __get_info(self):
        # Retrieves the network interfaces info and caches
        # them into the `self.network_info` dictionary.
        # In this way, if the user gets the ip address and 
        # then the gateway address for example, there is only
        # one call to the system to retrieve all the informations,
        # and not multiple calls like it was before.
        #
        # Raises a NetworkPropertiesException in case 
        # it is not possible to retrieve the network interface info.
        if self.check_superuser:
            self.__check_superuser()
        try:
            gateways = netifaces.gateways()
            gateway, interface = gateways['default'][netifaces.AF_INET]
            addrs = netifaces.ifaddresses(interface)
            self.network_info = addrs[netifaces.AF_INET][0]
            self.network_info['gateway'] = gateway
            self.network_info['interface'] = interface
            self.network_info['cidr'] = NetworkProperties.calc_cidr(self.netmask)
        except Exception as e:
            raise NetworkPropertiesException(
                "Can't get your internet IPv4 interface and address.\n"
                "Are you connected to the internet?\n"
                "The Exception message raised was:\n"
                "%s: %s" % (e.__class__.__name__, e.message))       

    def refresh(self):
        # Method used to refresh the network info without
        # allocating a new `NetworkInformation` object.
        # It deletes the information cached into the
        # `self.network_info` dictionary, and retrieves the
        # info again from the system.
        self.network_info = None
        self.__get_info()

    @property
    def ip_addr(self):
        # Returns the cached system ip address
        return self.network_info['addr']

    @property
    def netmask(self):
        # Returns the cached system netmask
        return self.network_info['netmask']
    
    @property
    def cidr(self):
        # Returns the cached system CIDR
        return self.network_info['cidr']

    @property
    def broadcast(self):
        # Returns the cached system broadcast address
        return self.network_info['broadcast']
    
    @property
    def gateway(self):
        # Returns the cached system gateway address
        return self.network_info['gateway']

    @property
    def interface(self):
        # Returns the cached system internet network interface
        return self.network_info['interface']

    def get_all_ips(self):
        # Get all IP from hostname
        with os.popen('hostname --all-ip-address') as ips:
            return ips.read()


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
