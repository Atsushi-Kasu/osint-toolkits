#!/bin/bash

# OSINT Toolkit Installer
# Made by Atsushi

echo "╔═══════════════════════════════════════════════════════════╗"
echo "║          OSINT Toolkit - Installation Script              ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

# Detect package manager
if [ -d "$PREFIX" ]; then
    PKG_MANAGER="pkg"
else
    PKG_MANAGER="apt"
fi

echo "[*] Updating packages..."
$PKG_MANAGER update -y && $PKG_MANAGER upgrade -y

echo "[*] Installing dependencies..."
$PKG_MANAGER install -y python python-pip git curl wget nmap whois dnsutils

echo "[*] Installing Python packages..."
pip install -r requirements.txt

echo "[*] Creating tools directory..."
mkdir -p ~/osint-tools

echo "[+] Installing theHarvester..."
git clone https://github.com/laramies/theHarvester ~/osint-tools/theHarvester 2>/dev/null || echo "[!] Already installed"

echo "[+] Installing Sublist3r..."
git clone https://github.com/aboul3la/Sublist3r ~/osint-tools/Sublist3r 2>/dev/null || echo "[!] Already installed"

echo "[+] Installing Sherlock..."
git clone https://github.com/sherlock-project/sherlock ~/osint-tools/sherlock 2>/dev/null || echo "[!] Already installed"

echo "[+] Installing Photon..."
git clone https://github.com/s0md3v/Photon ~/osint-tools/Photon 2>/dev/null || echo "[!] Already installed"

echo "[+] Installing SpiderFoot..."
git clone https://github.com/smicallef/spiderfoot ~/osint-tools/spiderfoot 2>/dev/null || echo "[!] Already installed"

echo ""
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║               Installation Complete! 🚀                   ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""
echo "Run with:"
echo "python3 osint.py"
