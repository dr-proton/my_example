import re

with open("log.txt", "r") as file:
    for line in file:
        match = re.search(r"Host (\S+) in vlan (\d+) .+ port (\S+) and port (\S+)", line)
        if match:
            data = match.group(1, 2, 3, 4)
            print(data)