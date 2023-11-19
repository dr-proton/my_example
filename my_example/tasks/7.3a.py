lst = []
j = 0
with open("CAM_table.txt", 'r') as f:
    for i in f:
        if "Gi" in i:
            lst.append(i.replace("DYNAMIC", '').split())
            lst[j][0] = int(lst[j][0])
            j += 1

lst.sort()
for i in lst:
    print(f"{i[0]:<8} {i[1]:>8} {i[2]:>10}")