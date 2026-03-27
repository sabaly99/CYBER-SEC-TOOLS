import socket
from IPy import IP

def domain_name_to_ip(ip_addr):
    try :
        IP(ip_addr)
        return(ip_addr)
    except ValueError:
        try:
            return socket.gethostbyname(ip_addr)
        except socket.gaierror:
            return None

ipaddress = input("[+] Enter Target to Scan: ").strip()
Actual_IP = domain_name_to_ip(ipaddress)
port = int(input('[+]Enter Target Port: '))

#first function
def port_scan():

    try:
        sock = socket.socket()
        sock.connect((Actual_IP,port))
        sock.settimeout(20)
        print(f"[+] Port {port} is OPEN")

    except:
        print(f"[-]Port {port} is CLOSED")

#second function
def scan_anyways(varr):
    try:
        soc = socket.socket()
        soc.connect((varr,port))
        print(f"[+] Port {port} is OPEN")
    
    except:
        print(f"[-]Port {port} is CLOSED")


if ',' in ipaddress:
    for A in ipaddress.split(','):
        target = domain_name_to_ip(A.strip())
        result = scan_anyways(target)
        print(result)  

else:
    pass
    

print(port_scan())