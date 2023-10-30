ip = "10.1.1.1"
lst = ip.split('.')
res = """
{:<8} {:<8} {:<8} {:<8}
{:08b} {:08b} {:08b} {:08b}
"""
print(res.format(int(lst[0]), int(lst[1]), int(lst[2]), int(lst[3]), int(lst[0]), int(lst[1]), int(lst[2]), int(lst[3])))