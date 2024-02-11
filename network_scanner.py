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
    answered_list=scapy.srp(arp_request_broadcast,timeout=1)[0]
    print(answered_list.summary())
    for host in answered_list:
        print(host[1].psrc)
        print(host[1].hwsrc)
        print("----------------------------------")



if __name__ == "__main__":
    scan("192.168.1.0/24")