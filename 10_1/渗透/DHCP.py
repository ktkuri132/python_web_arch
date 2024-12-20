from scapy.all import *

def send_dhcp_offer():
	# 构造 DHCP Offer 消息
	dhcp_offer = (
		Ether(src="02:42:ac:11:00:02", dst="ff:ff:ff:ff:ff:ff") /
		IP(src="192.168.1.1", dst="255.255.255.255") /
		UDP(sport=67, dport=68) /
		BOOTP(op=2, yiaddr="192.168.10.100", siaddr="192.168.1.1", chaddr="00:0c:29:68:22:8e") /
		DHCP(options=[
			("message-type", "offer"),
			("server_id", "192.168.1.1"),
			("lease_time", 600),
			("subnet_mask", "255.255.255.0"),
			("router", "192.168.1.1"),
			("name_server", "8.8.8.8"),
			"end"
		])
	)

	# 发送 DHCP Offer 消息
	sendp(dhcp_offer, iface="WLAN", verbose=1)

if __name__ == "__main__":
	while True:
		send_dhcp_offer()