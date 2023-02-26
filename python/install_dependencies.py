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
Attempting to Download Dependencies...
    """)

if line == 'NAME="Arch Linux"':
    os.system("sudo pacman -S budgie-screensaver gnome-bluetooth gnome-menus gnome-session gnome-settings-daemon gobject-introspection intltool meson sassc vala && cd ~/eagle-desktop/arch_dependencies && sudo pacman -U perl-html-tagset-3.20-13-any.pkg.tar.zst perl-http-date-6.05-6-any.pkg.tar.zst perl-encode-locale-1.05-10-any.pkg.tar.zst perl-http-negotiate-6.01-11-any.pkg.tar.zst libwnck3-43.0-3-x86_64.pkg.tar.zst")

if line == 'NAME="Manjaro"':
    os.system("sudo pacman -S budgie-screensaver gnome-bluetooth gnome-menus gnome-session gnome-settings-daemon gobject-introspection intltool meson sassc vala")

if line == 'NAME="Fedora"':
    os.system("sudo dnf install accountsservice-devel alsa-lib-devel desktop-file-utils gettext git glib2-devel gnome-bluetooth3.34-libs-devel gnome-desktop3-devel gnome-menus-devel gnome-settings-daemon-devel gobject-introspection-devel gsettings-desktop-schemas-devel gtk-doc gtk3-devel ibus-devel intltool json-glib-devel libX11-devel libXtst-devel libgee-devel libnotify-devel libpeas-devel libuuid-devel libwnck3-devel meson mutter-devel polkit-devel pulseaudio-libs-devel sassc upower-devel vala")

if line == 'NAME="Debian"':
    os.system("sudo apt install gnome-settings-daemon-dev gtk-doc-tools intltool libaccountsservice-dev libasound2-dev libgnome-bluetooth-dev libgnome-desktop-3-dev libgnome-menu-3-dev libgtk-3-dev libibus-1.0-dev libmutter-10-dev libpeas-dev libpolkit-agent-1-dev libpulse-dev libupower-glib-dev libwnck-3-dev meson ninja-build sassc uuid-dev valac git libgee-0.8-2 libgee-0.8-dev")

if line == 'NAME="Ubuntu"':
    os.system("sudo apt install gnome-settings-daemon-dev gtk-doc-tools intltool libaccountsservice-dev libasound2-dev libgnome-bluetooth-dev libgnome-desktop-3-dev libgnome-menu-3-dev libgtk-3-dev libibus-1.0-dev libmutter-10-dev libpeas-dev libpolkit-agent-1-dev libpulse-dev libupower-glib-dev libwnck-3-dev meson ninja-build sassc uuid-dev valac git libgee-0.8-2 libgee-0.8-dev")

if line == 'NAME="Linux Mint"':
    print(Fore.RED + "NOTE: There are many known issues about building Eagle Desktop on Linux Mint and it is not recommended.")
    print(Fore.WHITE + "")
    os.system("sudo apt install gnome-settings-daemon-dev gtk-doc-tools intltool libaccountsservice-dev libasound2-dev libgnome-bluetooth-dev libgnome-desktop-3-dev libgnome-menu-3-dev libgtk-3-dev libibus-1.0-dev libmutter-10-dev libpeas-dev libpolkit-agent-1-dev libpulse-dev libupower-glib-dev libwnck-3-dev meson ninja-build sassc uuid-dev valac git libgee-0.8-2 libgee-0.8-dev")

if line == 'NAME="Solus"':
    os.system("sudo eopkg it accountsservice-devel alsa-lib-devel gnome-bluetooth-devel gtk-doc gnome-settings-daemon-devel ibus-devel libgnome-desktop-devel libgnome-menus-devel libnotify-devel libpeas-devel libwnck-devel mutter-devel pulseaudio-devel sassc upower-devel vala ccache -c system.devel")

if line == 'NAME="Sabayon"':
    os.system("sudo equo i dev-util/re2c dev-libs/libsass dev-lang/sassc dev-util/intltool dev-util/ninja dev-util/itstool app-text/docbook-sgml-dtd app-text/docbook-dsssl-stylesheets dev-util/meson dev-util/gtk-doc-am app-text/yelp-tools dev-util/gtk-doc x11-libs/wxGTK app-eselect/eselect-wxwidgets")

else:
    print(f"""
I'm sorry, but something went wrong. Your Linux Distro may not support building Eagle Desktop from source. Try installing the dependencies manually if you can. 
If you really want to build Eagle Desktop from source but your distro isn't supported, you can request that your distro be added through github.
""")
