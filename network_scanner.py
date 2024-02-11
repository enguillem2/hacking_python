import scapy.all as scapy
import re

def scan(ip):
    # scapy.arping(ip)
    arp_request = scapy.ARP(pdst=ip)
    # scapy.ls(scapy.Ether())
    broadcast   = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # print(broadcast.summary())
    arp_request_broadcast = broadcast/arp_request
    # print(arp_request.summary())
    # arp_request_broadcast.show()

    #send BC packet
    answered_list=scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0]
    print("\t\t\tIp\t\t\tMAC\n------------------------------------------------------------")
    for host in answered_list:
        print(f"\t\t{host[1].psrc}\t\t{host[1].hwsrc}")



if __name__ == "__main__":
    scan("192.168.1.0/24")