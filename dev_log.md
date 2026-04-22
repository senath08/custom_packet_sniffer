## Bug Report: 2026-04-21 - Socket Initialization Failure

**Context:** Attempting to initialize a raw Python socket in Kali Linux to capture Layer 2 Ethernet frames.

**The Trigger:** Executed 'sudo python3 sniffer.py' containing the socket initialization string.

**The Error Output:**
'AttributeError: module 'socket' has no attribute :'ntohs''

**The Root Cause:** Syntax and Object-Oriented misalignment. The code incorrectly attempted to call 
the byte-order conversion function 'ntohs(3)' as a method of 'socket' *class* (via 'socket.socket.ntohs(3)').
However, 'ntohs(3)' is a *module-level* function built in Python's standard library.

**The Resolution:** Removed the chained class call and invoked the function directly from the module.
Failed Line     : 'conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.socket.ntohs(3))'
Corrected Line  : 'conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))'


## Bug Report: 2026-04-22 - TypeError in Protocol Formatting 

**Context:** Parsing the 14 byte Ethernet Header and printing Destination MAC, Source MAC and EtherType Protocol

**The Trigger:** Executed 'sudo python3 sniffer.py' with the protocol variable (integer) wrapped in MAC formatting function.

**The Error Output:**
'TypeError: 'int' object is not iterable (Traced to 'map{':02x'}.format, bytes_addr)'

**The Root Cause:** The MAC addresses were unpacked as byte strings ('6s'), which are iterable.
EtheyType Protocol is stored as an unsigned integer, which is not iterable.
Therefore, passing an non iterable 'int' object to 'map()' function creates a fatal TypeError.

**The Resolution:** Remove the protocol variable from the 'get_mac()' function.
Formatted the integer using 'hex(socket.htons(eth_proto))' to display the standard Hexadecimal EtherType.

