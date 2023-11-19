import re

log = 'Jun  3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'
match = re.search(r"Host (\S+) in vlan (\d+) .* port (\S+) and port (\S+)", log)
print(match)
print(match.group(0))
print(match.group(1))
print(match.group(2))
print(match.group(1, 2, 3))

match2 = re.search(r"Host (?P<mac>\S+) in vlan (?P<vlan>\d+) .* port (?P<intf1>\S+) and port (?P<intf2>\S+)", log)
print(match2.group("mac", "vlan", "intf1", "intf2"))
print(match2.groups())
print(match2.groupdict())



