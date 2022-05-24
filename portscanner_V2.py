import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

if len(sys.argv) == 2:
	
	# translate to IPv4
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid amount of Argument")

print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))


try:
	# scan ports between 1 to 100
	for port in range(1,100):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		
		# returns error 
		result = s.connect_ex((target,port))
		if result ==0:
			print("Port {} is open".format(port))
		s.close()
		
except KeyboardInterrupt:
		print("\n Exiting Program !!!!")
		sys.exit()
except socket.error:
		print("\ Server not responding !!!!")
		sys.exit()
