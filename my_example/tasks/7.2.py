import sys

file_name = sys.argv[1]
print(file_name)
with open("config_sw1.txt", 'r') as f:
    for item in f:
        if "!" in item:
            continue
        else:
            print(item.rstrip())