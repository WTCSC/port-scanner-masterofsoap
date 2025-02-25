import ipaddress
import socket
import sys
import argparse

def tcp_scan(ip, port, timeout=1):
    """Check if a given port is open on a given IP address."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((str(ip), port))
        sock.close()
        return result == 0  # Returns True if the port is open
    except socket.timeout:
        return False
    except Exception:
        return False

def parse_ports(port_arg):
    """Parses the -p argument to support single ports, ranges, and lists."""
    ports = set()
    if "," in port_arg:
        parts = port_arg.split(",")
        for part in parts:
            ports.update(parse_ports(part.strip()))
    elif "-" in port_arg:
        start, end = port_arg.split("-")
        ports.update(range(int(start), int(end) + 1))
    else:
        ports.add(int(port_arg))
    return sorted(ports)

def scan_network(cidr, ports):
    """Scan the given network for active hosts and open ports."""
    network = ipaddress.ip_network(cidr, strict=False)
    active_hosts = 0
    down_hosts = 0

    print(f"Scanning network {cidr} on ports {ports}...\n")

    for ip in network.hosts():
        open_ports = []
        for port in ports:
            if tcp_scan(ip, port):
                open_ports.append(port)

        if open_ports:
            print(f"{ip} (UP)")
            for port in open_ports:
                print(f"  - Port {port} (OPEN)")
            active_hosts += 1
        else:
            print(f"{ip} (DOWN)")
            down_hosts += 1

    print(f"\nScan complete. Found {active_hosts} active hosts, {down_hosts} down.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="IP and Port Scanner")
    parser.add_argument("-p", "--ports", required=True, help="Ports to scan (e.g., 80, 1-100, 22,443)")
    parser.add_argument("cidr", help="Network in CIDR format (e.g., 192.168.1.0/24)")
    
    args = parser.parse_args()

    try:
        ports = parse_ports(args.ports)
        scan_network(args.cidr, ports)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
