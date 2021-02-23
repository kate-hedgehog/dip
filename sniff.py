from scapy.all import *
import sys

ipa="192.168.220.63"
iface="eth0"

def psv_output(pkt):
    if pkt.haslayer(IP):
        #return pkt[IP].dst
        return pkt.command() # vse zagolovki

def myfilter(pkt):
    if pkt.haslayer(IP):
       return ((pkt[IP].dst == ipa) or (pkt[IP].src == ipa))

sniff(prn=psv_output, lfilter=myfilter, store=0)
