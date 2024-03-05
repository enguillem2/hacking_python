import scapy.all as scapy


packet = scapy.ARP(op=2,pdst="192.168.1.95",hwdst="30:b5:c2:ad:b6:14",psrc="192.168.1.1")
print("packet",packet)