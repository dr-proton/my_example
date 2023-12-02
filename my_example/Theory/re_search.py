import re

# ports = set()

# with open("log.txt", "r") as file:
#     for line in file:
#         match = re.search(r"Host (\S+) in vlan (\d+) .+ port (\S+) and port (\S+)", line)
#         if match:
#             ports.add(match.group(1, 2, 3, 4))
#             print(ports)

result = {}

with open("sh_cdp_neighbors_sw1.txt") as file:
    for line in file:
        if "Device ID" in line:
            host = re.search("Device ID: (\S+)", line).group(1)
            result[host] = {}
        elif "IP address" in line:
            ip = re.search("IP address: (\S+)", line).group(1)
            result[host]['ip'] = ip
        elif "Platform" in line:
            platform = re.search("Platform: (\S+ \S+)", line).group(1).strip(",")
            result[host]["platform"] = platform
        elif "Software" in line:
            ios = re.search("Cisco IOS Software, (.+),", line).group(1)
            result[host]['ios'] = ios
            
print(result)