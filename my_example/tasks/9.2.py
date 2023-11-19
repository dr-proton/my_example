trunk_mode_template = [
    "switchport mode trunk", "switchport trunk native vlan 999",
    "switchport trunk allowed vlan"
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17]
}

lst = []

def generate_trunk_config(*arg):
    for k,v in arg[0].items():
        lst.append(f"Interface {k}")
        for j in arg[1]:
            if "allowed" in j:
                lst.append(f"{j} {str(v).strip('[]')}")
            else:
                lst.append(f"{j}")
        
    return lst

generate_trunk_config(trunk_config, trunk_mode_template)

print(lst)