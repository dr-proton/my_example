

try:
    str1 = int(input("Введите номер влана: "))

    lst = []
    j = 0
    with open("CAM_table.txt", 'r') as f:
        for i in f:
            if "Gi" in i:
                lst.append(i.replace("DYNAMIC", '').split())
                lst[j][0] = int(lst[j][0])
                j += 1

    lst.sort()

    i = 0
    for item in lst:
        if str1 == item[0]:
            print(f"{item[0]:<6}{item[1]:>8}{item[2]:>10}")
except TypeError:
    print("Введите число!")