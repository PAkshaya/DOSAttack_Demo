#!/usr/bin/env/ python
import sys
from scapy.all import * 
flop = "false"
flopCount = 0
honeypot = "192.168.120.101"
assets = "192.168.140.101"

def pkt_callback(pkt):
	#print pkt.summary()
	global flop
	global flopCount
	global honeypot
	global assets
	if IP in pkt:
		if pkt[IP].dst == assets:
			flop = "false"
			print pkt[IP].dst + " to Assets"
		if pkt[IP].dst == honeypot and flop == "false":
			flop = "true"
			flopCount = flopCount + 1
			print pkt[IP].dst + "to Honeypot"
			print flopCount
			if flopCount == 10:
				print "REROUTING ALL ATTACKS TO HONEYPOT"
				print "Attacker has Flooded ASSETS 10 TIMES"
				os.system("iptables -t nat -D PREROUTING 1")
				sys.exit()
p = sniff(prn=pkt_callback)
