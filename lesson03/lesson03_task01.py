"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
   Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def dev(a, b):
    if b == 0:
        print("На ноль делить нельзя!")
    else:
        return a/b


a = input("Введите делимое: ")
if not a.isdigit():
    print('это не число')
    exit()
a = int(a)

b = input("Введите делитель: ")
if not b.isdigit():
    print('это не число')
    exit()
b = int(b)

result = dev(a,b)
print(f"Результат: {result:<0.2f}")