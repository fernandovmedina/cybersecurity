# imports python's built-in module for working with ip addresses and networks (e.g. "192.168.0.0/24")
import ipaddress
# imports from scapy: ARP builds arp packets, Ether builds ethernet frames, srp sends/receives at layer 2
from scapy.all import ARP, Ether, srp

# diferences between sr and srp (send and receive)
# sr:  sends and receive packets over the layer 3 of the OSI model, so it does not get the mac address
# srp: sends and receive packets over the layer 2 of the OSI model, so it does get the mac address of a device

# function to scan a network with arp requests
# "network: str" is a type hint, it says the argument is expected to be a string
def scan_with_arp(network: str):
  # converts the text to a network object, so ip_address module can work with it
  # strict=False allows host bits to be set (e.g. "192.168.0.15/24" is accepted and becomes 192.168.0.0/24)
  net = ipaddress.ip_network(network, strict=False)
  # builds the packet: an ethernet frame sent to the broadcast mac (every device on the local network receives it)
  # the "/" operator stacks layers, so the ARP request goes inside the ethernet frame
  # pdst is the target ip; passing the whole network makes scapy create one ARP request per ip in the range
  packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=str(net))
  # sends the packets at layer 2 and waits up to 2 seconds for replies; verbose=False hides scapy's output
  # srp returns two lists: answered (pairs of sent/received packets) and unanswered (ignored here with "_")
  answered, _ = srp(packet, timeout=2, verbose=False)

  # loops over every answered pair, sorted by the ip of the device that replied
  # p[1] is the received packet in each pair, and p[1].psrc is the ip address of the device that replied
  # ipaddress.ip_address(...) makes the sort numeric, so 192.168.0.2 comes before 192.168.0.10
  # "_" ignores the sent packet, "received" is the reply packet
  for _, received in sorted(answered, key=lambda p: ipaddress.ip_address(p[1].psrc)):
    # prints the ip of the device (padded to 16 characters so columns line up) followed by its mac address
    print(f"{received.psrc:16} {received.hwsrc}")

# this block only runs when the file is executed directly (python scan_network.py), not when it is imported
if __name__ == "__main__":
  # calls the function to scan every ip from 192.168.0.0 to 192.168.0.255
  scan_with_arp(network="192.168.0.0/24")
