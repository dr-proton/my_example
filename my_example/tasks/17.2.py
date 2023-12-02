import re
import csv

def parse_sh_version(data_file):
    lst = data_file.split("\n")
    attr_lst = []
    for data in lst:
        ios = re.search("Cisco IOS Software, (\S+).+, Version (?P<ios>\w+.?\w+.\w+.\w+)", data)
        image = re.search("System image (\w+) (\w+) (?P<img>\S+)", data)
        uptime = re.search("router uptime is (?P<uptime>\S+.+)", data)
        if ios:
            attr_lst.append(ios.group("ios").lstrip("("))
        if image:
            attr_lst.append(image.group("img").strip('"'))
        if uptime:
            attr_lst.append(uptime.group("uptime"))
    
    return  tuple(attr_lst)

    

def write_inventory_to_csv(data_filename, wr_file):
    headers = ["hostname", "ios", "image", "uptime"]
    with open(wr_file, "w") as f2:
        writer = csv.writer(f2, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(headers)

    for files in data_filename:
        host = files.split("_")[-1].split(".")[0]
        with open(files, "r") as f1, open(wr_file, "a+") as f2:
            res = list(parse_sh_version(f1.read()))
            res.insert(0, host)
            writer = csv.writer(f2, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(res)



if __name__ == "__main__":
    # lst = ["sh_version_r1.txt", "sh_version_r2.txt", "sh_version_r3.txt"]
    lst = ["sh_version_r1.txt", "sh_version_r2.txt", "sh_version_r3.txt", "sh_version_r4.txt"]
    write_inventory_to_csv(lst, "routers_inventory.csv")