""" The code is developed for Educational Purpose Only , learn and hack yourself
                      --> BY HACK WITH ROHIT TAMIL"""

import scapy.all as scapy
import pyfiglet

msg = pyfiglet.figlet_format("Hack With Rohit")
print(msg)

filename = input("Enter the IP range : ")
arp_pkt = scapy.ARP(pdst=filename)
# scapy.ls(scapy.ARP())
broadcast_pkt = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
combind_pkt = broadcast_pkt/arp_pkt
(answered_list,unanswered_list) = scapy.srp(combind_pkt,timeout=1)
answered_list.summary()
