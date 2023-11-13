import re

if __name__ == "__main__":
    print(r"\\data")
    int_line = '  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec,'
    res = re.search(r'MTU', int_line)
    print(res.group())

    res1 = re.search(r'BW \d+', int_line)
    print(res1.group())

    log2 = 'Oct  3 12:49:15.941: %SW_MATM-4-MACFLAP_NOTIF: Host f04d.a206.7fd6 in vlan 1 is flapping between port Gi0/5 and port Gi0/16'
    res2 = re.search(r'Host \S+', log2)
    print(res2.group())
