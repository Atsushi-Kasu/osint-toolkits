#!/usr/bin/env python3
"""
OSINT Toolkit - Advanced Intelligence Gathering Framework
Made by Atsushi
GitHub: https://github.com/[your-username]/osint-toolkit
"""

import os
import sys
import subprocess
import time
from datetime import datetime

__version__ = "2.0.0"
__author__ = "Atsushi"

# Colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'
BOLD = '\033[1m'

def clear():
    os.system('clear')

def banner():
    clear()
    print(f"""
{CYAN}{BOLD}
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║     ██████╗ ███████╗██╗███╗   ██╗████████╗               ║
║    ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝               ║
║    ██║   ██║███████╗██║██╔██╗ ██║   ██║                  ║
║    ██║   ██║╚════██║██║██║╚██╗██║   ██║                  ║
║    ╚██████╔╝███████║██║██║ ╚████║   ██║                  ║
║     ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝                  ║
║                                                           ║
║          ████████╗ ██████╗  ██████╗ ██╗     ███████╗     ║
║          ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝     ║
║             ██║   ██║   ██║██║   ██║██║     ███████╗     ║
║             ██║   ██║   ██║██║   ██║██║     ╚════██║     ║
║             ██║   ╚██████╔╝╚██████╔╝███████╗███████║     ║
║             ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝     ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
{RESET}
{MAGENTA}                    Made by Atsushi{RESET}
{YELLOW}            Advanced OSINT Intelligence Framework{RESET}
{GREEN}                  Version {__version__} - 2024{RESET}

""")

def print_menu(title, options):
    print(f"\n{BOLD}{CYAN}╔══════════════════════════════════════════════════════════╗{RESET}")
    print(f"{BOLD}{CYAN}║{YELLOW}  {title:^54}{CYAN}  ║{RESET}")
    print(f"{BOLD}{CYAN}╠══════════════════════════════════════════════════════════╣{RESET}")
    
    for key, value in options.items():
        print(f"{CYAN}║{RESET}  {GREEN}[{key}]{RESET} {WHITE}{value:47}{CYAN}║{RESET}")
    
    print(f"{BOLD}{CYAN}╚══════════════════════════════════════════════════════════╝{RESET}")

def execute_command(cmd, description):
    print(f"\n{YELLOW}[*] Executing: {description}{RESET}")
    print(f"{CYAN}[*] Command: {cmd}{RESET}\n")
    time.sleep(1)
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=False, text=True)
        if result.returncode == 0:
            print(f"\n{GREEN}[✓] Completed successfully!{RESET}")
        else:
            print(f"\n{RED}[✗] Command failed or tool not installed{RESET}")
    except Exception as e:
        print(f"\n{RED}[✗] Error: {str(e)}{RESET}")
    
    input(f"\n{YELLOW}Press Enter to continue...{RESET}")

# Menu functions
def menu_reconnaissance():
    while True:
        banner()
        print_menu("RECONNAISSANCE & INFORMATION GATHERING", {
            "1": "theHarvester - Email/Subdomain/IP Harvesting",
            "2": "Sublist3r - Advanced Subdomain Enumeration",
            "3": "Amass - Attack Surface Mapping",
            "4": "Recon-ng - Full Reconnaissance Framework",
            "5": "SpiderFoot - Automated OSINT Collection",
            "0": "Back to Main Menu"
        })
        
        choice = input(f"\n{GREEN}┌─[{CYAN}Atsushi{GREEN}@{CYAN}OSINT{GREEN}]─[{CYAN}Recon{GREEN}]\n└──╼ {WHITE}${RESET} ")
        
        if choice == "1":
            target = input(f"{YELLOW}Enter target domain: {RESET}")
            cmd = f"theHarvester -d {target} -l 500 -b all"
            execute_command(cmd, "theHarvester - Email/Subdomain Discovery")
        elif choice == "2":
            target = input(f"{YELLOW}Enter target domain: {RESET}")
            cmd = f"python3 ~/Sublist3r/sublist3r.py -d {target}"
            execute_command(cmd, "Sublist3r - Subdomain Enumeration")
        elif choice == "3":
            target = input(f"{YELLOW}Enter target domain: {RESET}")
            cmd = f"amass enum -passive -d {target}"
            execute_command(cmd, "Amass - Attack Surface Mapping")
        elif choice == "4":
            cmd = "recon-ng"
            execute_command(cmd, "Recon-ng - Interactive Framework")
        elif choice == "5":
            target = input(f"{YELLOW}Enter target: {RESET}")
            cmd = f"python3 ~/spiderfoot/sf.py -s {target}"
            execute_command(cmd, "SpiderFoot - Automated OSINT")
        elif choice == "0":
            break

def menu_social_media():
    while True:
        banner()
        print_menu("SOCIAL MEDIA INTELLIGENCE", {
            "1": "Sherlock - Username Search Across 300+ Sites",
            "2": "Social Mapper - Facial Recognition OSINT",
            "3": "Twint - Advanced Twitter Intelligence",
            "4": "Instagram-OSINT - Deep Instagram Analysis",
            "5": "OSRF - Username Search Framework",
            "0": "Back to Main Menu"
        })
        
        choice = input(f"\n{GREEN}┌─[{CYAN}Atsushi{GREEN}@{CYAN}OSINT{GREEN}]─[{CYAN}Social{GREEN}]\n└──╼ {WHITE}${RESET} ")
        
        if choice == "1":
            username = input(f"{YELLOW}Enter username: {RESET}")
            cmd = f"sherlock {username}"
            execute_command(cmd, "Sherlock - Username Hunter")
        elif choice == "2":
            image = input(f"{YELLOW}Enter image path: {RESET}")
            cmd = f"python3 ~/social_mapper/social_mapper.py -f {image} -m all"
            execute_command(cmd, "Social Mapper - Face Recognition")
        elif choice == "3":
            username = input(f"{YELLOW}Enter Twitter username: {RESET}")
            cmd = f"twint -u {username}"
            execute_command(cmd, "Twint - Twitter Intelligence")
        elif choice == "4":
            username = input(f"{YELLOW}Enter Instagram username: {RESET}")
            cmd = f"python3 ~/InstagramOSINT/main.py --username {username}"
            execute_command(cmd, "Instagram-OSINT Analysis")
        elif choice == "5":
            username = input(f"{YELLOW}Enter username: {RESET}")
            cmd = f"usufy.py -n {username} --platforms all"
            execute_command(cmd, "OSRF - Multi-Platform Search")
        elif choice == "0":
            break

def menu_network():
    while True:
        banner()
        print_menu("NETWORK & DOMAIN INTELLIGENCE", {
            "1": "Nmap - Advanced Network Scanning",
            "2": "Shodan - IoT/Server Search Engine",
            "3": "DNSRecon - DNS Enumeration Tool",
            "4": "Fierce - DNS Reconnaissance",
            "5": "WhatWeb - Web Technology Fingerprinting",
            "0": "Back to Main Menu"
        })
        
        choice = input(f"\n{GREEN}┌─[{CYAN}Atsushi{GREEN}@{CYAN}OSINT{GREEN}]─[{CYAN}Network{GREEN}]\n└──╼ {WHITE}${RESET} ")
        
        if choice == "1":
            target = input(f"{YELLOW}Enter target: {RESET}")
            cmd = f"nmap -sV -sC {target}"
            execute_command(cmd, "Nmap - Network Scanning")
        elif choice == "2":
            query = input(f"{YELLOW}Enter Shodan query: {RESET}")
            cmd = f"shodan search '{query}'"
            execute_command(cmd, "Shodan - IoT Search")
        elif choice == "3":
            target = input(f"{YELLOW}Enter domain: {RESET}")
            cmd = f"python3 ~/dnsrecon/dnsrecon.py -d {target}"
            execute_command(cmd, "DNSRecon - DNS Intelligence")
        elif choice == "4":
            target = input(f"{YELLOW}Enter domain: {RESET}")
            cmd = f"fierce --domain {target}"
            execute_command(cmd, "Fierce - DNS Recon")
        elif choice == "5":
            target = input(f"{YELLOW}Enter URL: {RESET}")
            cmd = f"whatweb {target}"
            execute_command(cmd, "WhatWeb - Technology Detection")
        elif choice == "0":
            break

def menu_email_phone():
    while True:
        banner()
        print_menu("EMAIL & PHONE INTELLIGENCE", {
            "1": "Holehe - Email to Account Finder",
            "2": "PhoneInfoga - Phone Number OSINT",
            "3": "Infoga - Email Information Gathering",
            "4": "EmailHarvester - Email Scraping",
            "5": "h8mail - Data Breach Search",
            "0": "Back to Main Menu"
        })
        
        choice = input(f"\n{GREEN}┌─[{CYAN}Atsushi{GREEN}@{CYAN}OSINT{GREEN}]─[{CYAN}Email{GREEN}]\n└──╼ {WHITE}${RESET} ")
        
        if choice == "1":
            email = input(f"{YELLOW}Enter email: {RESET}")
            cmd = f"holehe {email}"
            execute_command(cmd, "Holehe - Email Discovery")
        elif choice == "2":
            phone = input(f"{YELLOW}Enter phone: {RESET}")
            cmd = f"phoneinfoga scan -n {phone}"
            execute_command(cmd, "PhoneInfoga - Phone Intelligence")
        elif choice == "3":
            target = input(f"{YELLOW}Enter domain/email: {RESET}")
            cmd = f"python3 ~/Infoga/infoga.py --domain {target}"
            execute_command(cmd, "Infoga - Email OSINT")
        elif choice == "4":
            domain = input(f"{YELLOW}Enter domain: {RESET}")
            cmd = f"python3 ~/EmailHarvester/EmailHarvester.py -d {domain}"
            execute_command(cmd, "EmailHarvester")
        elif choice == "5":
            email = input(f"{YELLOW}Enter email: {RESET}")
            cmd = f"h8mail -t {email}"
            execute_command(cmd, "h8mail - Breach Search")
        elif choice == "0":
            break

def menu_advanced():
    while True:
        banner()
        print_menu("ADVANCED & DARKWEB INTELLIGENCE", {
            "1": "OnionSearch - Dark Web Search",
            "2": "Photon - Web Crawler for OSINT",
            "3": "Metagoofil - Metadata Extractor",
            "4": "Exiftool - Image Metadata",
            "5": "Maltego - Link Analysis",
            "0": "Back to Main Menu"
        })
        
        choice = input(f"\n{GREEN}┌─[{CYAN}Atsushi{GREEN}@{CYAN}OSINT{GREEN}]─[{CYAN}Advanced{GREEN}]\n└──╼ {WHITE}${RESET} ")
        
        if choice == "1":
            keyword = input(f"{YELLOW}Enter keyword: {RESET}")
            cmd = f"python3 ~/OnionSearch/onionsearch.py {keyword}"
            execute_command(cmd, "OnionSearch - Dark Web")
        elif choice == "2":
            target = input(f"{YELLOW}Enter URL: {RESET}")
            cmd = f"python3 ~/Photon/photon.py -u {target}"
            execute_command(cmd, "Photon - Web Crawler")
        elif choice == "3":
            domain = input(f"{YELLOW}Enter domain: {RESET}")
            cmd = f"python3 ~/metagoofil/metagoofil.py -d {domain} -t pdf"
            execute_command(cmd, "Metagoofil - Metadata")
        elif choice == "4":
            file = input(f"{YELLOW}Enter file path: {RESET}")
            cmd = f"exiftool {file}"
            execute_command(cmd, "Exiftool - Metadata")
        elif choice == "5":
            print(f"{CYAN}[i] Maltego requires GUI installation{RESET}")
            input(f"\n{YELLOW}Press Enter...{RESET}")
        elif choice == "0":
            break

def install_tools():
    banner()
    print(f"\n{YELLOW}[*] Installing OSINT tools...{RESET}\n")
    
    script_path = os.path.join(os.path.dirname(__file__), 'scripts', 'install.sh')
    if os.path.exists(script_path):
        subprocess.run(['bash', script_path])
    else:
        print(f"{RED}[!] Installer script not found{RESET}")
    
    input(f"\n{YELLOW}Press Enter to continue...{RESET}")

def about():
    banner()
    print(f"""
{CYAN}╔═══════════════════════════════════════════════════════════╗
║                     ABOUT OSINT TOOLKIT                   ║
╠═══════════════════════════════════════════════════════════╣{RESET}
║                                                           ║
║  {YELLOW}Developer:{RESET} Atsushi                                     ║
║  {YELLOW}Version:{RESET} {__version__}                                      ║
║  {YELLOW}GitHub:{RESET} github.com/[your-username]/osint-toolkit     ║
║                                                           ║
║  {GREEN}Description:{RESET}                                          ║
║  Advanced OSINT Framework with 25+ intelligence          ║
║  gathering tools in 5 categories.                        ║
║                                                           ║
║  {RED}⚠ Disclaimer:{RESET}                                          ║
║  For authorized security research only.                  ║
║  Unauthorized access is illegal.                         ║
║                                                           ║
{CYAN}╚═══════════════════════════════════════════════════════════╝{RESET}
""")
    input(f"\n{YELLOW}Press Enter to continue...{RESET}")

def main_menu():
    while True:
        banner()
        print_menu("MAIN MENU - SELECT CATEGORY", {
            "1": "Reconnaissance & Information Gathering",
            "2": "Social Media Intelligence",
            "3": "Network & Domain Intelligence",
            "4": "Email & Phone Intelligence",
            "5": "Advanced & DarkWeb Intelligence",
            "6": "Install/Update All Tools",
            "7": "About & Credits",
            "0": "Exit"
        })
        
        choice = input(f"\n{GREEN}┌─[{CYAN}Atsushi{GREEN}@{CYAN}OSINT{GREEN}]─[{CYAN}Main{GREEN}]\n└──╼ {WHITE}${RESET} ")
        
        if choice == "1":
            menu_reconnaissance()
        elif choice == "2":
            menu_social_media()
        elif choice == "3":
            menu_network()
        elif choice == "4":
            menu_email_phone()
        elif choice == "5":
            menu_advanced()
        elif choice == "6":
            install_tools()
        elif choice == "7":
            about()
        elif choice == "0":
            clear()
            print(f"\n{CYAN}Thank you for using OSINT Toolkit!{RESET}")
            print(f"{MAGENTA}Made by Atsushi{RESET}\n")
            sys.exit(0)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        clear()
        print(f"\n{RED}[!] Interrupted{RESET}\n")
        sys.exit(0)
