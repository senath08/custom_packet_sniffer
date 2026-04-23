# Custom Raw Packet Sniffer

A lightweight, low-level packet sniffer built entirely in Python. This tool bypasses standard operating system network abstractions to intercept, parse, and analyze raw network traffic at the Data Link (Layer 2) and Network (Layer 3) levels.

##  Objective
This project was developed to demonstrate a fundamental understanding of network transit, the OSI model, and raw socket manipulation. Rather than relying on high-level, third-party abstraction libraries (like Scapy or Npcap), this sniffer utilizes native Linux kernel capabilities to interact directly with raw hexadecimal byte streams.

##  Core Architecture & Features
* **Raw Socket Initialization:** Utilizes `AF_PACKET` and `SOCK_RAW` to hook directly into the Linux network interface, capturing unmodified frames before they reach the OS TCP/IP stack.
* **Byte-Level Parsing:** Implements Python's `struct` module to unpack Big-Endian network byte orders.
* **Layer 2 (Ethernet) Dissection:** Accurately slices the initial 14-byte frame to extract Destination MAC, Source MAC, and the EtherType Protocol.
* **Active Developer Log:** Detailed tracking of architectural constraints, OS-level permission handling, and byte-type debugging. (See `dev_log.md`).

##  Environment & Requirements
Because this tool requires direct interaction with the Data Link layer, it must be run in a Linux environment. Windows network stacks do not natively support `AF_PACKET` without third-party drivers.

* **OS:** Kali Linux (or any Linux distribution)
* **Language:** Python 3.x
* **Libraries:** `socket`, `struct`, `sys` (No external dependencies)
* **Permissions:** Root (`sudo`) access is strictly required to open raw sockets.

##  Usage Instructions

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/custom_packet_sniffer.git](https://github.com/YOUR_USERNAME/custom_packet_sniffer.git)
   cd custom_packet_sniffer
