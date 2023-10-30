command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
lst_vlan1 = set(command1.split()[-1].split(","))
lst_vlan2 = set(command2.split()[-1].split(","))

result = sorted(list(lst_vlan1 & lst_vlan2))
print(result)