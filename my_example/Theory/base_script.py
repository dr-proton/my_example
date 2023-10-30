from sys import argv

# access_template = ['switchport mode access',
#                    'switchport access vlan {}',
#                    'switchport nonegotiate',
#                    'spanning-tree portfast',
#                    'spanning-tree bpduguard enable']

# print('\n'.join(access_template).format(5))

# intf = argv[1]
# vlan = argv[2]

# access_template = ['switchport mode access',
#                    'switchport access vlan {}',
#                    'switchport nonegotiate',
#                    'spanning-tree portfast',
#                    'spanning-tree bpduguard enable']

# print(f"interface {intf}")
# print("\n".join(access_template).format(vlan))

access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

intf = input("Enter interface type and number: ")
vlan = input("Enter vlan id: ")

print(f"interface {intf}")
print("\n".join(access_template).format(vlan))