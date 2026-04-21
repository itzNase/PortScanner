# MadeByNase Port Scanner

A fast multi-threaded port scanner built in Python.

## Features
- Scans all 65,535 ports
- Multi-threaded (500 concurrent threads)
- Built-in progress bar
- Auto-detects invalid IPs
- Color-coded output
- Auto-installs dependencies

## Requirements
- Python 3.x
- colorama (auto-installed)

## Usage
Run the script:
python port_scanner.py

Then enter a target IP when prompted.

## Best Results
- 127.0.0.1 → your local machine (most reliable)
- 192.168.x.x → may be blocked by Windows Firewall
- scanme.nmap.org → public test server, always works

## Legal Notice
Only scan systems you own or have explicit permission to scan.
Unauthorized port scanning may be illegal in your country.

## Author
Made by Nase
