import socket
import struct

sock = socket.socket(socket.PF_PACKET,socket.SOCK_RAW,8)

dict = {}
print("Detection Start......")
D_val = 10 
D_val1 = D_val+10
while True:

    pkt = s.recvfrom(2048)
    ipheader = pkt[0][14:34]
    ip_hdr = struct.unpack("!8sB3s4s4s", ipheader)
    IP = socket.inet_ntoa(ip_hd)[3]
    print("Attack Ip", Ip)
    if IP in dict:
        dict[IP]=dict[IP]+1
        print(dict[IP])
    else:
        dict[IP] = 1