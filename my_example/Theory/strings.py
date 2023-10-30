vlan, mac, intf = ['100', 'aabb.cc80.7000', 'Gi0/1']
print("{:15} {:15} {:15}".format(vlan, mac, intf))
print(f"{vlan:15} {mac:15} {intf:15}")
print("{:.4f}".format(10.0/3))
print("{:b} {:b} {:b} {:b}".format(192, 168, 100, 1))
print("{:8b} {:8b} {:8b} {:8b}".format(192, 168, 100, 1))
print("{:08b} {:08b} {:08b} {:08b}".format(10, 1, 1, 1))
ip_template = """
IP address:
{:<8} {:<8} {:<8} {:<8}
{:08b} {:08b} {:08b} {:08b}
"""
print(ip_template.format(192, 168, 1, 1, 192, 168, 1, 1))