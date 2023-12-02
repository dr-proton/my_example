import yaml
from pprint import pprint

# with open("info.yml", "r", encoding="utf-8") as file:
#     data = yaml.safe_load(file)

# pprint(data)


to_yaml = {
   'access': ['switchport mode access',
              'switchport access vlan',
              'switchport nonegotiate',
              'spanning-tree portfast',
              'spanning-tree bpduguard enable'],
   'trunk': ['switchport trunk encapsulation dot1q',
             'switchport mode trunk',
             'switchport trunk native vlan 999',
             'switchport trunk allowed vlan'],
}

with open("info.yml", "w") as file:
    yaml.dump(to_yaml, file)