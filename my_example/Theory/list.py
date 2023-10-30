vlans = [10, 20, 30, 50]
print(vlans[2])

vlans[-1] = 99
print(vlans)

vlans.reverse()
print(vlans)

print(len(vlans))

new_vlans = sorted(vlans)
print(new_vlans)

vlans2 = [11, 12, 13, 14]
print(vlans2)

vlans2.append(9)
print(vlans2)

vlans3 = [21, 22, 23, 24]
vlans2.extend(vlans3)
print(vlans2)

print(vlans2.pop(-1))

vlans2.remove(22)
print(vlans2)

print(vlans2.index(9))

vlans2.insert(5, 10)
print(vlans2)

vlans2.sort()
print(vlans2)