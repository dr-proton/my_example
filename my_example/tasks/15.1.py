import re

def ge_ip_from_cfg(file1):
    lst = []
    with open(file1, 'r') as f:
        for data in f:
            res = re.search(r" ip address (?P<ip>[\d.]+).(?P<mask>[\d.]+)", data.rstrip())
            if res:
                lst.append(res.group("ip", "mask"))

    return lst

if __name__ == "__main__":
    res = ge_ip_from_cfg("config_r1.txt")
    print(res)