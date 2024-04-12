# make sure you made a copy of hosts before run this 

import os
import time

# Define the hosts file path for Ubuntu
hosts_path = "/etc/hosts"

# IP address to redirect the domains to (localhost)
redirect_ip = "127.0.0.1"

# Domains to block
block_list = [
    "www.youtube.com",
    "youtube.com",
    "m.youtube.com",
    "youtubei.googleapis.com",
    "youtube.googleapis.com",
    "www.youtube-nocookie.com"
]

# Markers to identify the block section in the hosts file
start_marker = "# Start of block section\n"
end_marker = "# End of block section\n"

def block_sites():
    with open(hosts_path, 'r+') as file:
        content = file.readlines()
        file.seek(0)  # Go to the beginning of the file
        for line in content:
            # Write all lines to the file except the old block section
            if start_marker in line:
                break  # Stop when the start marker is found
            file.write(line)
        file.truncate()  # Remove everything after the start marker
        
        # Write the new block section
        file.write(start_marker)
        for domain in block_list:
            file.write(f"{redirect_ip} {domain}\n")
        file.write(end_marker)
        print("Websites have been blocked.")

def unblock_sites():
    with open(hosts_path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        in_block_section = False
        for line in content:
            if line == start_marker:
                in_block_section = True  # Skip lines until the end marker
            elif line == end_marker:
                in_block_section = False
                continue  # Start writing again after the end marker
            if not in_block_section:
                file.write(line)
        file.truncate()  # Remove any leftovers from the block section
        print("Websites have been unblocked.")

if __name__ == "__main__":
    block_duration = 10800  # Duration to block the sites in seconds (3 hour)
    try:
        print("Blocking specified websites...")
        block_sites()
        time.sleep(block_duration)  # Block the sites for the specified duration
        print("Unblocking specified websites...")
        unblock_sites()
    except PermissionError:
        print("Error: Permission denied. Please run this script as root.")
