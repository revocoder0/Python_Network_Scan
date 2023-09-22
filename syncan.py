from scapy.all import *

ip = input("Enter ip address or url : ")
port = int(input("Enter the port number : "))

def checkhost():
    ping = IP(dst=ip)/ICMP()
    res = sr1(ping,timeout=1,verbose=0)
    if res == None:
        print("This host is down")
    else:
        print("This host is up")

def checkport():
    tcpRequest = IP(dst=ip)/TCP(dport=port,flags="S")
    tcpResponse=sr1(tcpRequest,timeout=1,verbose=0)
    try:
        if tcpResponse.getlayer(TCP).flags == "SA":
            print(port,"is listening")
    except AttributeError:
        print(port, "is listening")


checkhost()
checkport()