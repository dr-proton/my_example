with open("CAM_table.txt", 'r') as f:
    for i in f:
        if "Gi" in i:
            lst = i.replace("DYNAMIC", '').split()

print(lst)