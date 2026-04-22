import socket
import struct
import sys

# Helper function to format raw bytes into a readable MAC address (AA:BB:CC:DD:EE:FF)
def get_mac(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()

def main():
    # socket.AF_PACKET tells LInux to operate at Layer 2
    # socket.ntohs(3) tells the kernel to capture all Ethernet protocol
    try:
        conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
        print("[*] Raw socket successfully initialized.")
        print("[*] Listening for traffic... (Press Ctrl+C to stop)")

    except PermissionError:
        print("[!] Fatal: You must run this script with root priviledges")
        sys.exit(1)

    try:
        while True:
            # Capture raw packet data
            raw_data, addr = conn.recvfrom(65536)

            # Phase 1 Parsing: The Ethernet Header (First 14 bytes)
            # struct.unpack parameters:
            # '!' = Network bytes order (Big-Endian)
            # '6s' = 6 bytes (Destination MAC)
            # '6s' = 6 bytes (Source MAC)
            # 'H' = 2 bytes, unsigned short (EtherType Protocol)
            dest_mac, src_mac, eth_proto = struct.unpack('! 6s 6s H', raw_data[:14])
            print('\n[+] Ethernet Frame Captured:')
            print(f'    Destination MAC : {get_mac(dest_mac)}')
            print(f'    Source MAC      : {get_mac(src_mac)}')
            
            # Use socket.htons() to ensure that the integer is in the correct byte order for the OS
            # Also the final result is translated to hexadecimal for professional purpose
            print(f'    Protocol        : {hex(socket.htons(eth_proto))}')

    except KeyboardInterrupt:
        print("\n[*] Sniffer shutting down.")
        sys.exit(0)

if __name__ == '__main__':
    main()

