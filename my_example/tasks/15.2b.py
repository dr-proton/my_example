import re

def ge_ip_from_cfg(file1):
    dct = {}
    lst = []
    with open(file1, 'r') as f:
        for data in f:
            res1 = re.search(r"interface (?P<intf>\w+.\d)", data.rstrip())
            res2 = re.search(r"ip address (?P<ip>[\d.]+).(?P<mask>[\d.]+)", data.rstrip())
            res3 = re.search(r" ip address (?P<ip2>[\d.]+).(?P<mask2>[\d.]+) secondary", data.rstrip())
            if res1:
                intf_name = res1.group("intf")
                dct[intf_name] = {}
            elif res2:
                dct[intf_name] = [res2.group("ip", "mask")]
            if res3:
                dct[intf_name].append([res3.group("ip2", "mask2")])

        for k,v in dct.items():
            if not v:
                lst.append(k)
        
        for i in lst:
            dct.pop(i, None)

    return dct

if __name__ == "__main__":
    print(ge_ip_from_cfg("config_r2.txt"))
