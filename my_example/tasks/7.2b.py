import sys

ignore = ["duplex", "alias", "configuration"]

src_file = sys.argv[1]
dst_file = sys.argv[2]
with open(src_file, 'r') as f1, open(dst_file, 'a+') as f2:
    for i in f1:
        if ignore[0] in i:
            continue
        elif '!' in i:
            continue
        elif ignore[1] in i:
            continue
        elif ignore[2] in i:
            continue
        else:
            f2.write(i)