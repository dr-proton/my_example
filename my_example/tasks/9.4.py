ignore = ["duplex", "alias", "Current configuration"]
dct = {}

def convert_config_to_dict(config_filename):
    lst = []
    intf = ""
    with open(config_filename, 'r') as f:
        duplex, alias, cur_conf = ignore
        for i in f:
            if "!" in i:
                continue
            elif duplex in i:
                continue
            elif alias in i:
                continue
            elif cur_conf in i:
                continue
            else:
                lst.append(i.rstrip())

    for c in range(len(lst)):
        if lst[c]:
            if lst[c].startswith(" ") and not lst[c-1].startswith(" "):
                intf = lst[c-1]
                dct[intf] = [lst[c].strip()]
            elif lst[c].startswith(" "):
                dct[intf].append(lst[c].strip())
            elif not lst[c].startswith(" ") and not lst[c-1].startswith(" ") and not lst[c+1].startswith(" "):
                dct[lst[c]] = []

    return dct
               
            
res = convert_config_to_dict("config_sw1.txt")
print(res)