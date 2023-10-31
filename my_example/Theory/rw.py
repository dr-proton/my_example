# f = open("my_example/Theory/test1.txt", "r")
# print(f.read())
# print(f.readline())
# for item in f:
#     print(item)
# print(f.readlines())
# print(f.read().split("\n"))

cfg_lines = ['!',
'service timestamps debug datetime msec localtime show-timezone year',
'service timestamps log datetime msec localtime show-timezone year',
'service password-encryption',
'service sequence-numbers',
'!',
'no ip domain lookup',
'!',
'ip ssh version 2',
'!']

file1 = "my_example/Theory/r2.txt"

f = open(file1, 'w')
str1 = "\n".join(cfg_lines)
# f.write(str1)
f.writelines(str1)
f.close()
