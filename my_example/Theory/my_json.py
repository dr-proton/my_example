import json

# with open("sw_templates.json", "r", encoding="utf-8") as file:
#     data = json.load(file)

# print("=" * 100)

# for k,v in data.items():
#     print(k)
#     print("\n".join(v))

# with open("sw_templates.json", "r", encoding="utf-8") as file:
#     data = file.read()

# data_json = json.loads(data)

# for k,v in data_json.items():
#     print(k)
#     print("\n".join(v))


trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk native vlan 999', 'switchport trunk allowed vlan'
]

access_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

to_json = {"trunk": trunk_template, "acess": access_template}

with open("sw_template1.json", "w", encoding="utf-8") as file:
    json.dump(to_json, file, indent=2)

