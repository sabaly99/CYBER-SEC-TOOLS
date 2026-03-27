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

# Parse ports (single, range, multiple)
def parse_ports(port_input):
    ports = []

    # Range (e.g. 20-100)
    if '-' in port_input:
        start, end = port_input.split('-')
        ports = list(range(int(start), int(end) + 1))

    # Multiple ports (e.g. 22,80,443)
    elif ',' in port_input:
        ports = [int(p.strip()) for p in port_input.split(',')]

    # Single port
    else:
        ports = [int(port_input)]

    return ports

ipaddress = input("[+] Enter Target to Scan: ").strip()
Actual_IP = domain_name_to_ip(ipaddress)
port_input = input("[+] Enter port(s) (e.g. 80 OR 20-100 OR 22,80,443): ").strip()
ports = parse_ports(port_input)
#port = int(input('[+]Enter Target Port: '))

#first function
#def port_scan():

   # try:
   #     sock = socket.socket()
   #     sock.settimeout(20)
  #      sock.connect((Actual_IP,port))
#       print(f"[+] Port {port} is OPEN")
#
   # except:
    #    print(f"[-]Port {port} is CLOSED")

#second function
def scan_anyways(varr):
    try:
        soc = socket.socket()
        soc.settimeout(60)
        soc.connect((varr,port))
        print(f"[+] Port {port} is OPEN")
    
    except:
        print(f"[-]Port {port} is CLOSED")


#MULTI-TARGET CASE
if ',' in ipaddress:
    for A in ipaddress.split(','):
        target = A.strip()
        I_P = domain_name_to_ip(target)
        for port in ports:
            
            scan_anyways(I_P)  

else:
    ip = domain_name_to_ip(ipaddress)
    for port in ports:
        scan_anyways(ip)

