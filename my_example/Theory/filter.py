lst = ["1", "2", "4", "3"]
res = list(filter(lambda x: int(x) % 2 == 1, lst))
print(res)

lst = ["1", "2", "a", "3"]
res = list(filter(str.isdigit, lst))
print(res)

ip = "10.1.1.1"
print(list(filter(str.isdigit, ip.split("."))))
print(list(map(str.isdigit, ip.split("."))))

print([i for i in lst if i.isdigit()])
