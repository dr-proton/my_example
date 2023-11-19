lst1 = [1,2,3]
lst2 = [4,5,6]

print(list(zip(lst1, lst2)))


lst3 = [1,2,3]
lst4 = [4,5,6,7]
lst5 = [8,9,10]

print(list(zip(lst3, lst4, lst5)))

print(dict(list(zip(lst1, lst2))))