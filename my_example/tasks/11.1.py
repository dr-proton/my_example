def parse_cdp_neighbors(arg1):
    dct = {}
    lst = arg1.split()
    loc_host = lst[0].split(">")[0]
    res = lst[lst.index("Port") + 2:]
    i = 0
    intf_name_loc = ""
    while i < len(res):
        if "Eth" in res[i] or "Gi" in res[i]:
            if not intf_name_loc:
                rem_host = res[i-1]
                intf_name_loc = res[i]
                intf_num_loc = res[i+1]
            else:
                intf_name_rem = res[i]
                intf_num_rem = res[i+1]
                dct[(loc_host, intf_name_loc + intf_num_loc)] = (rem_host, intf_name_rem + intf_num_rem)
                intf_name_loc = ""
        i += 1

    return dct

if __name__ == "__main__":
    with open("sh_cdp_n_r3.txt", 'r') as f:
        print(parse_cdp_neighbors(f.read()))
