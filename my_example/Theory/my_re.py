import re

# print(r"\\data")

if __name__ == "__main__":
    int_line = '  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec,'
    res = re.search(r'MTU', int_line)
    print(res.group())
