# f = open("my_example/Theory/test1.txt", "r")
# print(f.read())
# print(f.readline())
# for item in f:
#     print(item)
# print(f.readlines())
# print(f.read().split("\n"))

# cfg_lines = ['!',
# 'service timestamps debug datetime msec localtime show-timezone year',
# 'service timestamps log datetime msec localtime show-timezone year',
# 'service password-encryption',
# 'service sequence-numbers',
# '!',
# 'no ip domain lookup',
# '!',
# 'ip ssh version 2',
# '!']

# file1 = "my_example/Theory/r2.txt"

# f = open(file1, 'w')
# str1 = "\n".join(cfg_lines)
# # f.write(str1)
# f.writelines(str1)
# f.close()

# with open('my_example/Theory/r2.txt', 'r') as f, open('my_example/Theory/r4.txt', 'w') as dest:
#     for item in f:
#         dest.write(item)

# result = {}

# with open('my_example\Theory\sh_ip_int_br.txt', 'r') as file1:
#     for item in file1:
#         lst = item.split()
#         if lst and lst[1][0].isdigit():
#             result[lst[0]] = lst[1]

# print(result)

# with open('my_example\Theory\sh_ip_interface.txt', 'r') as file1:
#     for item in file1:
#         if "line protocol " in item:
#             inter = item.split()[0]
#         elif "MTU is" in item:
#             inter_mtu = item.split()[2]
#             print(f"{inter} {inter_mtu:>8}")

res = {}        

with open('my_example\Theory\sh_ip_interface2.txt', 'r') as file1:
    for item in file1:
        if "line protocol" in item:
            intf = item.split()[0]
        elif "Internet address" in item:
            ip = item.split()[-1]
        elif "MTU is" in item:
            intf_mtu = item.split()[2]
            res[intf] = [ip, intf_mtu]

for k,v in res.items():
    print(f"{k:20}{v[0]:25}{v[-1]}")