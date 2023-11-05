access_mode_template = [
    "switchport mode access", "switchport access vlan",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security"
]

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}

def generate_access_config(intf_vlan_mapping, *access_template, psecurity=None):
    lst = []
    for k,v in intf_vlan_mapping.items():
        lst.append(f"Interface {k}")
        if psecurity:
            for i in access_template[0]:
                if "vlan" in i:
                    lst.append(f"{i} {v}")
                else:
                    lst.append(i)
    
            for j in access_template[1]:
                    lst.append(f"{j}")
        else:
             for i in access_template[0]:
                if "vlan" in i:
                    lst.append(f"{i} {v}")
                else:
                    lst.append(i)

    return lst

res1 = generate_access_config(access_config, access_mode_template)
res2 = generate_access_config(access_config, access_mode_template, port_security_template, psecurity=True)

print("\n".join(res1), "\n")
print("\n".join(res2))