# -*- coding: utf-8 -*-

# This is just a work-around for a Python2.7 issue causing
# interpreter crash at exit when trying to log an info message.
try:
    import logging
    import multiprocessing
except:
    pass

import sys
py_version = sys.version_info[:2]

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.md')) as f:
    CHANGES = f.read()


testpkgs = [
]


install_requires = [
    "netifaces"
]


setup(
    name='ping-network',
    version='0.0.1',
    description='a tool that ping usable hosts in your network except the network address itself and the network broadcast address',
    long_description=README + "\n\n" + CHANGES,
    author='Dario Lynx',
    author_email='',
    url='https://github.com/dariolynx/ping_network',
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=testpkgs,
    entry_points={
        'console_scripts': [
            'ping_network = ping_network:main'
        ]
    },
    zip_safe=True
)

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
