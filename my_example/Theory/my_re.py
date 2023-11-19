import re

# if __name__ == "__main__":
#     print(r"\\data")
#     int_line = '  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec,'
#     res = re.search(r'MTU', int_line)
#     print(res.group())

#     res1 = re.search(r'BW \d+', int_line)
#     print(res1.group())

# log2 = 'Oct  3 12:49:15.941: %SW_MATM-4-MACFLAP_NOTIF: Host f04d.a206.7fd6 in vlan 1 is flapping between port Gi0/5 and port Gi0/16'
# res2 = re.search(" Host (\S+) in vlan (\d+) is flapping between port (\S+) and port (\S+)", log2).groups()
# print(res2)

# log3 = '*Jul  7 06:15:18.695: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/3, changed state to down'
# res3 = re.search(r"\d+:\d+:\d+", log3).group()
# print(res3)

# log4 = 'Jun  3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'
# res4 = re.search(r"\w+\.\w+\.\w+", log4).group()
# print(res4)

# log5 = 'Ethernet0/1    192.168.200.1   YES NVRAM  up          up'
# res5 = re.search(r"\d+\.\d+\.\d+\.\d+", log5).group()
# print(res5)

# log6 = '1500     aab1.a1a1.a5d3    FastEthernet0/1'
# lst = re.search(r"\d+\s+\S+", log6).group().split()
# print(lst)

# email1 = 'user1@gmail.com'
# res6 = re.search("\w+@\w+\.\w+", email1).group()
# print(res6)

# email2 = 'user2.user1.test@gmail.com'
# res7 = re.search("\S+@\w+\.\w+", email2).group()
# print(res7)


# cdp = '''
#  SW1#show cdp neighbors detail
#  -------------------------
# Device ID: SW2
#     Entry address(es):
#     IP address: 10.1.1.2
# Platform: cisco WS-C2960-8TC-L,  Capabilities: Switch IGMP
# Interface: GigabitEthernet1/0/16,  Port ID (outgoing port): GigabitEthernet0/1
# Holdtime : 164 sec'''

# res8 = re.search("(Fast|Gigabit).+", cdp).group()
# print(res8)

# log7 = "100     aa12.35fe.a5d3    FastEthernet0/1"
# res8 = re.search("^\d+", log7).group()
# print(res8)


# log8 = 'SW1#show cdp neighbors detail'
# res9 = re.search("^.+#", log8).group()
# print(res9)

# log9 = "100     aa12.35fe.a5d3    FastEthernet0/1"
# res10 = re.search("\S+$", log9).group()
# print(res10)

# log10 = "100     aa12.35fe.a5d3    FastEthernet0/1"
# res11 = re.search(r"\S+$", log10).group()
# print(res11)

# log11 = ['SW1#show cdp neighbors detail', 'SW1>sh ip int br', 'r1-london-core# sh ip route']

# for item in log11:
#     print(re.search(r"^.+[>#]", item).group())

# log11 = "FastEthernet0/1            10.0.12.1       YES manual up                    up"
# res12 = re.search("(\S+)\s+([\w.]+)", log11)
# # print(res12.group(0))
# print(res12[1])
# print(res12[2])

# res13 = re.search(r"(?P<intf>\S+)\s+(?P<ip>[\d.]+)\s+", log11)
# print(res13.group('intf'))
# print(res13.group('ip'))
# print(res13.groupdict())

# line = '00:09:BB:3D:D6:58  10.1.10.2 86250   dhcp-snooping   10  FastEthernet0/1'
# match = re.search(r"(?P<mac>\S+) +(?P<address>\S+) +\d+ +\S+ +(?P<vlan>\d+) +(?P<intf>\S+)", line)
# print(f"MAC: {match.group('mac')}\nIP: {match.group('address')}\nVLAN ID: {match.group('vlan')}\nInterface: {match.group('intf')}")
# lst = []
# req = r"(?P<mac>\S+) +(?P<address>\S+) +\d+ +\S+ +(?P<vlan>\d+) +(?P<intf>\S+)"

# with open("dhcp_snooping.txt", 'r') as data:
#     for item in data:
#         res = re.search(req, item)
#         if res:
#             lst.append(res.groupdict())

# for i, j in enumerate(lst, 1):
#     print(f"\nПараметры устройства: {i}")
#     for k,v in j.items():
#         print(f"\t{k}: {v}")

bgp = '''
 R9# sh ip bgp | be Network
Network          Next Hop       Metric LocPrf Weight Path
192.168.66.0/24  192.168.79.7                       0 500 500 500 i
*>                  192.168.89.8                       0 800 700 i
 *  192.168.67.0/24  192.168.79.7         0             0 700 700 700 i
*>                  192.168.89.8                       0 800 700 i
*  192.168.88.0/24  192.168.79.7                       0 700 700 700 i
 *>                  192.168.89.8         0             0 800 800 i
 '''
for item in bgp.split("\n"):
    match = re.search(r"(?P<as>\d+) (?P=as)", item)
    if match:
        print(item)