def sum(a, b): return a + b

print(sum(2, 4))

res_sum = lambda a,b: a + b
print(res_sum(3, 2))

lst_vl = [("office", 12), ("iptv", 10), ("mgmt", 8)]

print(sorted(lst_vl, key=lambda a: a[1]))
print(lst_vl[1])