import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="Interface to change its MAC address")
    parser.add_option("-m","--mac",dest="new_mac",help="New MAC address")
    (options,arguments) = parser.parse_args()

    if not options.interface:
        #code to handle error
        parser.error("[-] Please epecify an interface, use --help for info")
    elif not options.new_mac:
        #code to handle error
        parser.error("[-] Please epecify a mac, use --help for info")
        
    return options



def change_mac(interface,mac):
    print(f"[+] changinc MAC of {interface} to {mac}")
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac])
    subprocess.call(["ifconfig",interface,"up"])


def get_current_mac_address(interface):
    ifconfig_res=subprocess.check_output(["ifconfig",interface])
    theMac=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig_res))

    if theMac:
        return theMac.group(0)
    return None



options=get_arguments()
inital_mac=get_current_mac_address(options.interface)
print(f"initial mac {inital_mac}")
if inital_mac == None:
    print("no mac interface")
    exit(1)
if inital_mac!=options.new_mac:
    change_mac(options.interface,options.new_mac)
    theMac=get_current_mac_address(options.interface)
    if theMac==options.new_mac:
        print("mac changed succesfully")
    else:
        print("mac not changed")
else:
    print("mac is the same")
