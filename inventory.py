#!/usr/bin/env python3

import json
import subprocess

network = "192.168.104.0/24"

scan = subprocess.check_output(
    f"nmap -p 5985 --open {network} -oG -",
    shell=True
).decode()

hosts = []

for line in scan.splitlines():
    if "5985/open" in line:
        ip = line.split()[1]
        hosts.append(ip)

inventory = {
    "windows": {
        "hosts": hosts,
        "vars": {
            "ansible_connection": "winrm",
            "ansible_port": 5985,
            "ansible_winrm_transport": "ntlm",
            "ansible_winrm_server_cert_validation": "ignore"
        }
    }
}

print(json.dumps(inventory, indent=2))
