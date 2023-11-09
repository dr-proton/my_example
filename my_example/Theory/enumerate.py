list1 = ['str1', 'str2', 'str3']

for i, j in enumerate(list1):
    print(i, j)

list1 = ['str1', 'str2', 'str3']

for i, j in enumerate(list1, 100):
    print(i, j)

print(list(enumerate(list1, 100)))