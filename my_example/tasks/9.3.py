def get_int_vlan_map(config_filename):
    mode_access = {}
    mode_trunk = {}

    with open(config_filename, 'r') as f:
        for i in f:
            if "interface" in i:
                intf = i.split()[-1]
            elif "trunk allowed" in i:
                # mode_trunk[intf] = i.split()[-1].split()
                lst_vl = i.split()[-1].split(',')
                mode_trunk[intf] = [int(vl) for vl in lst_vl]
            elif "access vlan" in i:
                mode_access[intf] = int(i.split()[-1])
            
        return (mode_trunk, mode_access)


res = get_int_vlan_map("config_sw1.txt")
print(res[1])