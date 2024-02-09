import scapy.all as scapy

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
    answered,unanswered=scapy.srp(arp_request_broadcast,timeout=1)
    print(answered.summary())


if __name__ == "__main__":
    scan("192.168.1.0/24")