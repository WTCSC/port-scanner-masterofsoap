IP and Port Scanner

Description

This script scans a given CIDR network for active hosts and identifies open ports on those hosts. It supports scanning single ports, port ranges, and lists of ports.

Features

Scans a specified network range (CIDR format)

Identifies active (UP) hosts

Supports single ports, port ranges, and lists of ports (e.g., -p 80, -p 1-100, -p 22,443,3306)

Displays only open ports for active hosts

Implements timeout for better performance

Usage

Running the Script

python scanner.py -p <ports> <cidr>

Example Commands

Scan a single port (80) in a network:

python scanner.py -p 80 192.168.1.0/24

Scan a range of ports (1-100):

python scanner.py -p 1-100 192.168.1.0/24

Scan multiple specific ports (80, 443, 3306):

python scanner.py -p 80,443,3306 192.168.1.0/24

Example Output

Scanning network 192.168.1.0/24 on ports [80, 443]...

192.168.1.10 (UP)
  - Port 80 (OPEN)
  - Port 443 (OPEN)
192.168.1.11 (DOWN)
192.168.1.12 (UP)
  - Port 80 (OPEN)
Scan complete. Found 2 active hosts, 1 down.

Requirements

Python 3.x

Installation

Clone the repository:

git clone <repo-url>
cd <repo-directory>

Run the script with the desired parameters.

Notes

Only scans hosts that respond to the TCP connection request.

The script uses a timeout to prevent long delays.

License

This project is open-source and available under the MIT License.