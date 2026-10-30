# Code to list all the devices on a network
from scapy.all import ARP, Ether, srp

network = str(input("Enter the network (192.168.1.0/24): "))

# get all the devices on the network
def scan(network: str):
  packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=network)
  answered, _ = srp(packet, timeout = 2, verbose = False)

  for _, received in answered:
    print(f"{received.psrc:16} {received.hwsrc}")

scan(network)
