import socket 
from binascii  import hexlify
ip_addr1='127.0.0.1'
ip_addr2='192.168.0.1'
packed_ip1=socket.inet_aton(ip_addr1)
unpacked_ip1=socket.inet_ntoa(packed_ip1)
print "packed:%s, unpacked:%s" %(hexlify(packed_ip1),unpacked_ip1)

