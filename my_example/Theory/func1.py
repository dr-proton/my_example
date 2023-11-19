# def sum_arg(a, *args):
#     print(a, args)
#     return a + sum(args)


# sum_arg(2, 3, 3)

# def sum_arg(a, **kwargs):
#     print(a, kwargs)
#     return a + sum(kwargs.values())

# sum_arg(3, b=10, c=12)

# items = [1,2,3]

# res = "one: {} tho: {} three: {}".format(*items)
# print(res)

# interfaces_info = [['Fa0/1', '10.0.1.1', '255.255.255.0'],
#                     ['Fa0/2', '10.0.2.1', '255.255.255.0'],
#                     ['Fa0/3', '10.0.3.1', '255.255.255.0'],
#                     ['Fa0/4', '10.0.4.1', '255.255.255.0'],
#                     ['Lo0', '10.0.0.1', '255.255.255.255']]

# for item in interfaces_info:
#     print("Interface: {}\nIP: {}\nMask: {}".format(*item))

users = [{"user1": "admin"},{"user2": "admin"}, {"user3": "admin"}, {"user4": "admin"}]

print(*users)