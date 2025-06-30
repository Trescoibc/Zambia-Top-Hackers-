#!/bin/bash
echo -e "\e[32mInstalling Zambia Top Hackers Tool...\e[0m"
pkg update && pkg upgrade -y
pkg install python -y
pkg install git -y
pkg install whois curl nmap -y
pip install requests pyfiglet colorama speedtest-cli
echo -e "\n\e[32mDone! Run with:\e[0m python zth_toolkit.py"
