import os.path
import os
import linecache
import re
import colorama
from colorama import *

file1 = open('/etc/os-release', 'r')

line = linecache.getline("/etc/os-release", 1).rstrip('\n')

regex = re.compile('NAME="(.*)"')

os_name = regex.search(line).group(1)

print(f'Hello, {os_name} User!')
print("""
Attempting to Build...
    """)

if line == 'NAME="Debian"':
    os.system("cd ~/eagle-desktop && meson build --prefix=/usr --libdir=/usr/lib -Dwith-gnome-screensaver=true && ninja -j$(($(getconf _NPROCESSORS_ONLN)+1)) -C build && sudo ninja -C install")

if line == 'NAME="Ubuntu"':
    os.system("cd ~/eagle-desktop && meson build --prefix=/usr --libdir=/usr/lib -Dwith-gnome-screensaver=true && ninja -j$(($(getconf _NPROCESSORS_ONLN)+1)) -C build && sudo ninja -C install")

if line == 'NAME="Linux Mint"':
    print(Fore.RED + "NOTE: There are many known issues about building Eagle Desktop on Linux Mint and it is not recommended.")
    print(Fore.WHITE + "")
    os.system("cd ~/eagle-desktop && meson build --prefix=/usr --libdir=/usr/lib -Dwith-gnome-screensaver=true && ninja -j$(($(getconf _NPROCESSORS_ONLN)+1)) -C build && sudo ninja -C install")

if line == 'NAME="Solus"':
    os.system("cd ~/eagle-desktop && meson --prefix /usr --libdir /usr/lib64 --sysconfdir /etc -Dwith-stateless=true build --buildtype plain && ninja -j$(($(getconf _NPROCESSORS_ONLN)+1)) -C build && sudo ninja -C install")

else:
    os.system("cd ~/eagle-desktop && meson build --prefix=/usr --sysconfdir=/etc && ninja -j$(($(getconf _NPROCESSORS_ONLN)+1)) -C build && sudo ninja -C install")