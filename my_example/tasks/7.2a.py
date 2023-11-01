import sys

ignore = ["duplex", "alias", "configuration"]

file_name = sys.argv[1]
with open("config_sw1.txt", 'r') as f:
    for i in f:
        if ignore[0] in i:
            continue
        elif '!' in i:
            continue
        elif ignore[1] in i:
            continue
        elif ignore[2] in i:
            continue
        else:
            print(i.rstrip())