import struct
import socket
from random import randint
import time
def checksum(data):
    s = 0
    n = len(data) % 2
    for i in range(0, len(data)-n, 2):
        s+= (data[i]) + ((data[i+1]) << 8)
    if n:
        s+= (data[i+1])
    while (s >> 16):
        s = (s & 0xFFFF) + (s >> 16)
    s = ~s & 0xFFFF
    return s

def icmp():
    type=8
    code=0
    chksum=0
    id=randint(0,0xFFFF)
    seq=1
    real_chksum=checksum(struct.pack("!BBHHH",type,code,chksum,id,seq))
    icmp_pkt=struct.pack("!BBHHH",type,code,socket.htons(real_chksum),id,seq)
    return icmp_pkt


s = socket.socket(socket.AF_INET, socket.SOCK_RAW,1)

ip=('192.168.56.101',3000) //ip addr you want to ping to
s.connect((ip))

print("Ready.")
print("Ctrl-C to quit.")
print("Sending 'DONE' shuts down the server and quits.")
while True:
    s.send(icmp())
    time.sleep(1)
