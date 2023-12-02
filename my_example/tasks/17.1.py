import csv
import re

def write_dhcp_snooping_to_csv(file1, file2):
    lst = []
    host = file1.split("_")[0]
    with open(file1, "r", encoding="utf-8") as f1, open(file2, "w") as f2:
        for data in f1:
            res = re.search(r"(?P<mac>\S+) +(?P<ip>\S+) +\d+ +\S+ +(?P<vlan>\d+) +(?P<port>\S+)", data)
            if res:
                lst.append([host, res.group("mac"), res.group("ip"), res.group("vlan"), res.group("port")])

        writer = csv.writer(f2)
        for data in list(lst):
            writer.writerow(data)

                
write_dhcp_snooping_to_csv("sw1_dhcp_snooping.txt", "test17_1.csv")
