lst = ["mike", "bob", "john"]
print(list(map(str.capitalize, lst)))

lst2 = ["1","2","3","4"]
print(list(map(int, lst2)))

lst3 = [1, 2, 3, 4]
vlans = [100, 110, 150, 200]

print(list(map(lambda x: "vlan {}".format(x), vlans)))

print([int(i) for i in lst2])
print([int(i) * 2 for i in lst2])
print([f"vlan {item}" for item in vlans])
print(list(map(int, lst2)))

print(list(map(lambda i, j: i*j, lst3, vlans)))