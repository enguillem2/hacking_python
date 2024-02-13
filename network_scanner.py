import scapy.all as scapy
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a","--address",dest="address",help="Address to scan")
    options = parser.parse_args()

    if not options.address:
        #code to handle error
        parser.error("[-] Please epecify an address, use --help for info")
        
    return options




def scan(ip):
    hosts=[]
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
    for host in answered_list:
        h={}
        h["ip"]=host[1].psrc
        h["mac"]=host[1].hwsrc
        hosts.append(h)

    return hosts

def print_host(host):
    # print("------------------------------------------------------------")
    # print("\t\t\tIp\t\t\tMAC\n------------------------------------------------------------")
    print(f"\t\t{host['ip']}\t\t{host['mac']}")



if __name__ == "__main__":
    # os.system('clear')
    options=get_arguments()
    address=options.address
    hosts=scan(address)
    # print(hosts)
    print("\t\t\tIp\t\t\tMAC\n------------------------------------------------------------")
    for host in hosts:
        print_host(host)