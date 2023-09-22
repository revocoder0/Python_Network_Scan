from scapy.all import *

print("################# ##########")
print("####         ##   #########")
print("####        ##    ##")
print("####       ##     ##")
print("####      ##      ##")
print("###########       ##########")
print("####   ##         ##########")
print("####    ##        ##")
print("####     ##       ##")
print("####       ##      ############ This Tools Created By Han Niux")
print("Edit by RevoCoder\n\n")

host = input("Enter your target : ")
ip = socket.gethostbyname(host)
port = int(input("Enter Port : "))

def is_up(ip):
    icmp = IP(dst=ip)/ICMP()
    resp = sr1(icmp,timeout=10)
    if resp == None:
        return False
    else:
        return True
def probe_port(ip,port,result = 1):
    src_port = RandShort()
    try:
        p = IP(dst=ip)/TCP(sport=src_port,dport=port,flags='A',seq=12345)
        resp = sr1(p,timeout=2)#Sending Packet
        if str(type(resp)) == "<type 'NoneType'>":
            result = 1
        elif resp.haslayer(TCP):
            if resp.getlayer(TCP).flags == 0x4:
                result = 0
            elif (int(resp.getlayer(ICMP).type)==3 and int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
                result = 1
    except Exception as e:
        pass
    return result

if __name__ == '__main__':
    conf.verb = 0
    if is_up(ip):
        response = probe_port(ip, port)
        if response == 1:
            print("Filtered | Stateful Firewall present")
        elif response == 0:
            print("Unfiltered | Stateful firewall absent")
    else:
        print("Host is Down")