

infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]

def create_network_map(arg1):
    dct = {}
    for f in arg1:
        with open(f, 'r') as file1:
            for i in file1:
                if ">" in i.strip():
                    loc_host = i.strip().split(">")[0]
                elif "Eth" in i.strip():
                    rem_host = i.strip().split()[0]
                    intf_name_loc = i.strip().split()[1]
                    intf_num_loc = i.strip().split()[2]
                    intf_name_rem = i.strip().split()[-2]
                    intf_num_rem = i.strip().split()[-1]
                    dct[(loc_host, intf_name_loc + intf_num_loc)] = (rem_host, intf_name_rem + intf_num_rem)

    return dct


if __name__ == "__main__":
    print(create_network_map(infiles))

