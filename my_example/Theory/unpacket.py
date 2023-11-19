interface = ['FastEthernet0/1', '10.1.1.1', 'up', 'up']

intf, ip, status, protocol = interface
# print(intf)

line = '100    01bb.c580.7000    DYNAMIC     Gi0/1'

vlanid, mac, _, intf = line.split()
# print(vlanid)

vlans = [10, 11, 13, 30]

first, *rest = vlans
print(first, rest)

cdp = 'SW1     Eth 0/0    140   S I   WS-C3750-  Eth 0/1'
name, l_intf, *other, r_intf = cdp.split()
# print(name, l_intf)
# print(other)
# print(r_intf)

with open("../tasks/CAM_table.txt", 'r') as f:
    for item in f:
        print(item.rstrip())