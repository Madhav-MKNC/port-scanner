import socket
import sys

from time import time
init = time()

if len(sys.argv) not in [4,5]:
    print("-"*70)
    print(" USAGE --> python port-scan.py HOST_NAME START_PORT END_PORT TIMEOUT")
    print("-"*70)
    sys.exit()

print("+"+"-"*21+"+")
print("|","SIMPLE PORT SCANNER","|")
print("+"+"-"*21+"+\n+")
timeout = float(input('=> Set timeout (=0.01 for fact scan with low accuracy; =1 for vice-versa): ')) if len(sys.argv) != 5 else float(sys.argv[4])

try:
    host = socket.gethostbyname(sys.argv[1])
except socket.gaierror as e:
    print(e)
    sys.exit()

openports = list()
try:
    i=1
    for port in range(int(sys.argv[2]),int(sys.argv[3])+1):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(timeout)
        no_connection = s.connect_ex((host,port))
        print(f'+ Scanning port {port}...',end="\r")
        if not no_connection:
            openports.append(port)
            # banner = s.recv(1024) ## banner grabbing for some extra info
            output = f'[{i}] OPEN port {port}'
            print(output+' '*(50-len(output)))
            i+=1
    #    print(connection)
        s.close()
except KeyboardInterrupt:
    pass

# for i in openports:
#     print(f'+ port {i} OPEN')

if not openports:
    print('NO PORT OPEN IN THE GIVEN RANGE')

print("+"+' '*50)
print("scanned %d ports in %f seconds\n"%(port,time()-init))
    
input('program finished')