import re

def parse_sh_ip_int_br(file):
    lst = []
    with open(file, "r") as f:
        for data in f:
            res = re.search(r"(?P<intf>\S+) +(?P<ip>[\d.]+).+(?P<st>up|down|administratively down) +(?P<pr>up|down)", data.strip())
            if res:
                lst.append(res.group("intf", "ip", "st", "pr"))
        
    return lst

if __name__ == "__main__":
    print(parse_sh_ip_int_br("sh_ip_int_br.txt"))
