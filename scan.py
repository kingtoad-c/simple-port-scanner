import socket
import sys 

try:
    target = input("Enter target IP address: ")
    port_range = input("Enter port range (e.g., 20-80): ")
    start_port, end_port = map(int, port_range.split('-'))

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        sock.close()

except KeyboardInterrupt:
    print("\nScan stopped by user.")
    sys.exit()
except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()
except socket.error:
    print("\nCouldn't connect to server.")
    sys.exit()
