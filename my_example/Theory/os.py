import ipaddress

ip = ipaddress.ip_address("10.1.1.1")
print(ip)
print(ip.is_private)
print(ip + 5)
print(ip)
subnet1 = ipaddress.ip_network('80.0.1.0/28')
print(subnet1)
print(subnet1.with_netmask)
print(subnet1.with_hostmask)
print(subnet1.with_prefixlen)
print(subnet1.prefixlen)
print(subnet1.num_addresses)
print(list(subnet1.hosts()))
print(list(subnet1.subnets()))
print(list(subnet1.subnets(prefixlen_diff=2)))
print(list(subnet1.subnets(new_prefix=30)))

IP1 = '10.0.1.1'
IP2 = '10.0.1.0/24'

print(ipaddress.ip_network(IP1))
print(ipaddress.ip_network(IP2))