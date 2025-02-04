import socket
import termcolor

def scan(target, ports):
    print('\n' + ' Starting scan for ' + str(target) + ' on ports: ' + str(ports))
    for port in range(1, ports):
        scan_port(target, port)
        

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(f"Port {port} is open")
    except:
        pass
        
targets = input("[*] Enter targets to scan(split them by \",\") \n : ")
ports = input("[*] Enter how many ports you want to scan: ")

if ',' in targets:
    print(termcolor.colored(("[*] Scanning multiple targets"), 'green'))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), int(ports))
else:
    scan(targets, int(ports))

