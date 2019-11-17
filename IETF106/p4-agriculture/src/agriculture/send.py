#!/usr/bin/env python

import argparse
import sys
import socket
import random
import struct
from scapy.all import sendp, send, hexdump, get_if_list, get_if_hwaddr, bind_layers
from scapy.all import Packet, IPOption
from scapy.all import Ether, IP, UDP
from scapy.all import IntField, FieldListField, FieldLenField, ShortField, PacketListField, LongField
from scapy.layers.inet import _IPOption_HDR
from scapy.fields import *

from time import sleep

def get_if():
    ifs=get_if_list()
    iface=None # "h1-eth0"
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break
    if not iface:
        print "Cannot find eth0 interface"
        exit(1)
    return iface

class Agri(Packet):
    fields_desc = [ IntField("id", 0),
                  IntField("pH", 0),
                  IntField("temp", 0)]

bind_layers(Ether, IP)
bind_layers(IP, Agri)

# Usage ./send.py DEST_ADDR
def main():
    addr = socket.gethostbyname(sys.argv[1])
    ph = raw_input('Enter pH Value : ')
    ph = float(ph)
    ph = int('0x' + (struct.pack('!f', ph).encode('hex')), 16)

    temp = raw_input('Enter temperature (degree Celcius) : ')
    temp = float(temp)
    temp = int('0x' + (struct.pack('!f', temp).encode('hex')), 16)
    iface = get_if()

    pkt = Ether(dst='08:00:00:00:01:22',type=0x800) / IP(dst=addr, proto=143) /  Agri(id=0x1234, pH=ph, temp=temp)
    pkt.show2()
    sendp(pkt, iface=iface, verbose=False)

if __name__ == '__main__':
    main()
