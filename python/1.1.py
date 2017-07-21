import socket
def print_machine_info():
	hostname=socket.gethostname()
	ip_addr=socket.gethostbyname(hostname)
	print "hostname: %s" %hostname
	print "ip_addr: %s" %ip_addr
if __name__ == '__main__':
	print_machine_info()