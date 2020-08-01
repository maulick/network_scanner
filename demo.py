import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    arp_request.show()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    scapy.arping(ip)

scan("10.0.2.1/24")
