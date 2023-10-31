lst = {}
with open('ospf.txt', 'r') as f:
    for item in f:
        print(f"Pref{item.split()[1]:>32}\nAD/Mertic{item.split()[2].strip('[]'):>21}\nNext-Hop{item.split()[4].strip(','):>25}\nLast update{item.split()[5].strip(','):>18}\nOutbound Interface{item.split()[6]:>21}\n")

