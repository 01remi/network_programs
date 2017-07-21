import socket
from binascii import hexlify
def function_do_things():
	for ip_address in ['127.0.0.1','192.168.1.1']:
		packed_ip=socket.inet_aton(ip_address)
		unpacked_ip=socket.inet_ntoa(packed_ip)
		print "IP Address: %s , packed:%s , unpacked:%s" %(ip_address,hexlify(packed_ip),unpacked_ip)

if __name__ == '__main__':
	function_do_things()