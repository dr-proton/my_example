import re

def parse_sh_cdp_neighbors(file):
    host = re.search("(\S+)>", file).group().split(">")[0]
    dct = {host: {}}
    res = re.findall("(\w+) +(\w+ \d+/\d+) +(\d+) +(\w+ )+ +(\d+) +(\w+ \d+/?\d+)", file)
    for item in res:
        dct[host].update({item[1]: {item[0]: item[-1]}})

    print(dct)

if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt", "r") as file:
        res = file.read()
        parse_sh_cdp_neighbors(res)