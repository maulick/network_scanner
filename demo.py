import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    arp_request.show()
    
    scapy.arping(ip)

scan("10.0.2.1/24")
