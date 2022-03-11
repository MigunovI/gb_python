"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
   и возвращает сумму наибольших двух аргументов.
"""


def my_func(a,b,c):
    a,b,c = sorted((a,b,c), reverse=True)
    return a + b


a = input("Введите первое число: ")
if not a.isdigit():
    print('это не число')
    exit()
a = int(a)

b = input("Введите второе число: ")
if not b.isdigit():
    print('это не число')
    exit()
b = int(b)

c = input("Введите третье число: ")
if not c.isdigit():
    print('это не число')
    exit()
c = int(c)

print(my_func(a,b,c))
