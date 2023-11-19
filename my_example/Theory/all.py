ip = '10.0.1.1'

res = all(i.isdigit() for i in ip.split('.'))
print(res)

lst1 = [False, True, True, True]
print(all(lst1))