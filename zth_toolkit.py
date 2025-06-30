# zth_toolkit.py

import os
import requests
import time
import pyfiglet
from colorama import Fore, Style

def banner():
    os.system("clear")
    print(Fore.GREEN + pyfiglet.figlet_format("Zambia Hackers", font="slant"))
    print(Fore.WHITE + "Created by: Zambia Top Hackers 🇿🇲\n")

def ip_lookup():
    print("\n[+] IP Lookup")
    ip = input("Enter IP (or leave blank for your own): ").strip()
    url = f"https://ipinfo.io/{ip if ip else ''}/json"
    data = requests.get(url).json()
    for key in data:
        print(f"{key}: {data[key]}")
    input("\nPress Enter to continue...")

def website_scanner():
    print("\n[+] Website Scanner")
    site = input("Enter website (e.g. google.com): ").strip()
    os.system(f"whois {site}")
    input("\nPress Enter to continue...")

def phone_lookup():
    print("\n[+] Phone Info Checker")
    phone = input("Enter phone number with country code (e.g. +26097...): ").strip()
    print("Checking number...")
    print("Demo only. Upgrade API to enable real lookup.")  # Placeholder
    input("\nPress Enter to continue...")

def speed_test():
    print("\n[+] Speed Testing...")
    os.system("speedtest")

def main_menu():
    while True:
        banner()
        print(Fore.CYAN + "[1] IP Lookup")
        print("[2] Website Scanner")
        print("[3] Phone Info Checker")
        print("[4] Internet Speed Test")
        print("[5] Exit\n")
        choice = input(Fore.YELLOW + "Enter your choice: ")

        if choice == "1":
            ip_lookup()
        elif choice == "2":
            website_scanner()
        elif choice == "3":
            phone_lookup()
        elif choice == "4":
            speed_test()
        elif choice == "5":
            print(Fore.GREEN + "\nGoodbye hacker 👋")
            break
        else:
            print(Fore.RED + "Invalid option!")
            time.sleep(1)

main_menu()
