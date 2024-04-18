"""
This script temporarily blocks access to specified websites by modifying the system's hosts file.
It is specifically tailored for Ubuntu and requires root permissions due to the need to write to /etc/hosts.

The script works by:
1. Adding entries to the hosts file that redirect listed domains to the localhost IP ('127.0.0.1').
2. After a set duration, these entries are removed to unblock the sites.

Requirements:
- Python 3.x
- Root privileges

Usage:
- Execute this script as root to avoid permission errors.
- The script blocks the sites for a predefined duration and then automatically unblocks them.

Warning:
- Modifying the hosts file can affect system operations. Always ensure you have a backup of the original hosts file before running this script.
"""

import os
import time
import subprocess

# Define the hosts file path for Ubuntu
hosts_path = "/etc/hosts"

# IP address to redirect the domains to (localhost)
redirect_ip = "127.0.0.1"

# Markers to identify the block section in the hosts file
start_marker = "# Start of block section\n"
end_marker = "# End of block section\n"


def flush_dns_cache():
    """Flushes the system DNS cache."""
    try:
        subprocess.run(["sudo", "systemd-resolve", "--flush-caches"], check=True)
        print("DNS cache flushed successfully.")
    except subprocess.CalledProcessError:
        print("Failed to flush DNS cache. Make sure you have the necessary permissions.")



# Function to block sites
def block_sites(block_list):
    """Blocks a list of websites by redirecting their domain names to localhost in the hosts file."""
    with open(hosts_path, 'r+') as file:
        # Read existing content and remove old block section
        content = file.readlines()
        file.seek(0)
        for line in content:
            if start_marker in line:
                break
            file.write(line)
        file.truncate()
        
        # Add new block section with domains from block_list
        file.write(start_marker)
        for domain in block_list:
            file.write(f"{redirect_ip} {domain}\n")
        file.write(end_marker)
        print("Websites have been blocked.")

# Function to unblock sites
def unblock_sites():
    """Removes entries from the hosts file that were added to block sites, effectively unblocking them."""
    with open(hosts_path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        in_block_section = False
        for line in content:
            if line == start_marker:
                in_block_section = True
            elif line == end_marker:
                in_block_section = False
                continue
            if not in_block_section:
                file.write(line)
        file.truncate()
        print("Websites have been unblocked.")

if __name__ == "__main__":
    block_duration = 10800  # Duration to block the sites in seconds (3 hours)
    try:
        flush_dns_cache()
        # Load block list from a file
        with open("block-list.txt", "r") as f:
            block_list = [line.strip() for line in f if line.strip()]

        print("Blocking specified websites...")
        block_sites(block_list)
        time.sleep(block_duration)
        print("Unblocking specified websites...")
        unblock_sites()
    except PermissionError:
        print("Error: Permission denied. Please run this script as root.")
    except FileNotFoundError:
        print("Error: 'block_list.txt' not found. Ensure the file exists in the same directory as this script.")

