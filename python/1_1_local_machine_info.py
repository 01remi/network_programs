import socket

def print_machine_info():
	hostname= socket.gethostname();
	Ip_address= socket.gethostbyname(hostname);
	print "Host Name: %s" %hostname
	print "IP address: %s" %Ip_address

if __name__ == '__main__':
	print_machine_info()