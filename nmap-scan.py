import nmap

scanner = nmap.PortScanner()

print(scanner.scan('localhost'))
