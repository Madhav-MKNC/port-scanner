""" 
This is a simple but very fast port scanner. It is able to scan for 10000 open ports in less than 10 seconds.
We need to improve the accuracy.

NEW FEATURE:  	get live status on a port.
				specify it in sys.argv parameters as => 'python port-scan.py <hostname> -p<port>'
				where <port1> is replaced by your specified port
				full command eg: python port-scan.py localhost -p22

by: Madhav MKNC
"""

# imports
import socket
import sys
from time import time as now
from time import sleep 

# usage
def usage():
	print("-"*100)
	print(f"USAGE [for port scaning]     --> python3 {sys.argv[0]} HOST_NAME START_PORT END_PORT")
	print(f"                             --> python3 {sys.argv[0]} HOST_NAME")
	print(f"      [for port live status] --> python3 {sys.argv[0]} HOST_NAME -p PORT")
	print("-"*100)
	sys.exit()

# print screen
def printScreen(): 
	print("+"+"-"*21+"+")
	print("|","SIMPLE PORT SCANNER","|")
	print("+"+"-"*21+"+\n")

# connecting to a port
def port_open(host, port):
	try:
		with socket.socket() as s:
			socket.setdefaulttimeout(TIMEOUT)
			connection = s.connect_ex((host, int(port)))
			return not bool(connection)
	except Exception as err:
		print(f"[!] error connecting to {host}:{port}")
		print("[ERROR]",err)
		return False

# live status of a port 
def live_rePORTS(host, port):
	try:
		print(f"[=] live status of port:{port} on host:{host}")
		while True:
			if port_open(host, port): print(f'[+] port {port} - OPEN    ',end='\r')
			else: print(f'[-] port {port} CLOSED\t',end='\r')
			sleep(3) # next iteration waits for 3 seconds
	except KeyboardInterrupt:
		sys.exit()

# port scanner
def scanports(host, start_port, end_port):
	init = now()
	openports = list()

	try:
		i=1
		for port in range(int(start_port),int(end_port)+1):
			print(f"[ ] Scanning port {port}",end='\r')
			if port_open(host, port):
				openports.append(port)
				print(f"[{i}] port - {port} - OPEN")
				i += 1 
	except KeyboardInterrupt:
		print("\n[-] keyboard interrupted")

	if not openports:
		print('NO PORT OPEN IN THE GIVEN RANGE')
	print("[+] scanned %d ports in %f seconds\n"%(port,now()-init))


if __name__ == "__main__":
	printScreen()

	if '-h' in sys.argv or 'help' in sys.argv:
		usage()
	
	try:
		if '-p' in sys.argv:
			if len(sys.argv)!=4: usage()
			live_rePORTS(sys.argv[1], sys.argv[3])
		elif len(sys.argv) == 2:
			TIMEOUT = int(input("[+] Set Timeout: "))
			scanports(sys.argv[1], 1, 65535)
		elif len(sys.argv) == 4:
			TIMEOUT = int(input("[+] Set Timeout: "))
			HOST, START, END = map(str,sys.argv[1:])
			scanports(HOST, START, END)
		else:
			usage()

	except Exception as e: 
		print("[ERROR]",e)
