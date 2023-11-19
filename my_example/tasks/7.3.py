with open("CAM_table.txt", 'r') as f:
    for i in f:
        if "Gi" in i:
            lst = i.replace("DYNAMIC", '').split()
            print(f"{lst[0]:8}{lst[1]}{lst[2]:>10}")