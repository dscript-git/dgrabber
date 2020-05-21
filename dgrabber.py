#!/usr/bin/env python3

import socket
import os

#colors
red = '\033[91m'
yellow = '\033[93m'
white = '\033[97m'
green = '\033[92m'
info = '\033[93m[!]\033[0m'
good = '\033[92m[+]\033[0m'

# Linux OS specific commands
os.system('apt-get install neofetch')
os.system('clear')
os.system('neofetch --ascii_distro debian --logo')

# Start of the script
print (green," ===> 'SIMPLE DGRABBER v1.0' by dscript-git <=== ")

name = input('\033[97m'"Enter Your Name: "'\033[91m')
grabber = socket.socket()
ip = input('\033[97m'"Enter target ip: "'\033[93m')
port = int(input('\033[97m'"Enter target port: "'\033[93m'))

grabber.connect((ip,port))

result = grabber.recv(1024)

print (good, result)

grabber.close()
print ()
print ('\033[93m'"Thank you for appreciating my simple code " + info,name + '\033[93m'"!!!")
