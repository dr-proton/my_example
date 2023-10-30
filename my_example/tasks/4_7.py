mac = "AAAA:BBBB:CCCC"
lst1 = bin(int(mac.split(":")[0], 16))[2:]
lst2 = bin(int(mac.split(":")[1], 16))[2:]
lst3 = bin(int(mac.split(":")[2], 16))[2:]

print(f"{lst1}{lst2}{lst3}")