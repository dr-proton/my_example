item = ["10", "20", "30", "b", "40"]
lst = [int(vl) for vl in item if vl.isdigit()]

# print(lst)

london_co = {
    'r1' : {
    'hostname': 'london_r1',
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.1'
    },
    'r2' : {
    'hostname': 'london_r2',
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.2'
    },
    'sw1' : {
    'hostname': 'london_sw1',
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '3850',
    'ios': '3.6.XE',
    'ip': '10.255.0.101'
    }
}

# res = [london_co[device]['ios'] for device in london_co]
# print(res)

# vlans = [[10, 21, 35], [101, 115, 150], [111, 40, 50]]
# res = [vlan for lst_vlan in vlans for vlan in lst_vlan]
# print(res)

vlans = [100, 110, 150, 200]
names = ['mngmt', 'voice', 'video', 'dmz']

res = ["vlan {}\n name {}".format(vlan, name) for vlan, name in zip(vlans, names)]
print("\n".join(res))