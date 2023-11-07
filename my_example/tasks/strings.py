lst1 = ["1","2","3","4","5"]
lst2 = ["2","4"]

# for i in lst1:
#     for j in lst2:
#         if j in i:
#             print(i)

ignore = ["duplex", "alias", "Current configuration"]

j = 0

for i in lst1:
    while j < len(lst2):
        if lst2[j] in i:
             continue
        else:
            print(i)
        j += 1