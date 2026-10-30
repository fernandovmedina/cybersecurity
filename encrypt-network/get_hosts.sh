#!/bin/bash

# code to get all the hosts on a network using bash
# the first three octets of the network to scan (192.168.0.0/24)
prefix="192.168.0"

# walk through all the hosts of the network
for i in {1..254}; do
  {
  # ping each host so the system sends an arp request first to resolve its mac address
  # we don't care about the ping reply: hosts that ignore ping still answer arp, and end up in the arp cache
  # on macOS -W is in milliseconds, so 1000 waits 1 second
  ping -c 1 -W 1000 "$prefix.$i" > /dev/null 2>&1
  } &
done

# wait for all the pings running in the background to finish
wait

# read the arp cache (-a all entries, -n don't resolve hostnames)
# each line looks like: ? (192.168.0.1) at aa:bb:cc:dd:ee:ff on en0 ifscope [ethernet]
# keep only the ips of our network, skip unresolved and broadcast entries, and print the ip and mac
arp -an | awk -v prefix="$prefix." '
  {
    # removes the parenthesis around the ip
    ip = substr($2, 2, length($2) - 2)
    mac = $4
    if (index(ip, prefix) == 1 && mac != "(incomplete)" && mac != "ff:ff:ff:ff:ff:ff") {
      # macOS drops leading zeros (e.g. "3:85"), so pad every byte to two digits ("03:85")
      n = split(mac, bytes, ":")
      mac = ""
      for (b = 1; b <= n; b++) {
        mac = mac (b > 1 ? ":" : "") (length(bytes[b]) == 1 ? "0" : "") bytes[b]
      }
      printf "%-16s %s\n", ip, mac
    }
  }
' | sort -t . -k4,4n
