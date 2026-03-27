import socket
from IPy import IP


ipaddress = input("[+] Enter Target to Scan: ")
port = int(input('[+]Enter Target Port: '))

try:
    sock = socket.socket()
    sock.connect((ipaddress,port))
    print(f"[+] Port {port} is OPEN")

except:
    print(f"Port {port} is CLOSED")