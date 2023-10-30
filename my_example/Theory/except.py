# try:
#     2 / 0
#     print("Cool!")
# except ZeroDivisionError:
#     print("Делить на ноль нельзя")
# except ValueError:
#     print("Введите число")

try:
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    res = int(a) / int(b)
except ZeroDivisionError:
    print("Делить на ноль нельзя")
except ValueError:
    print("Введите число")
else:
    print(res)
finally:
    print("Этот блок выполнится в любом случае")