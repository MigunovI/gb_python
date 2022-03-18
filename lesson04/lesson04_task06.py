"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
   Обратите внимание, что создаваемый цикл не должен быть бесконечным.
   Необходимо предусмотреть условие его завершения.

   Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
   Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from itertools import cycle, count


def generator(start,stop):
    for el in count(start):
        if el > stop:
            break
        else:
            print(el)


start = input('С какого числа начинать итерацию: ')
repeats_count = input('Сколько чисел вывести: ')
try:
    start = int(start)
    repeats_count = max(int(repeats_count),0)
except ValueError:
    print("Неверный ввод")
    exit()
generator(start, start + repeats_count)



def repeate(some_list, count):
    iterator = cycle(some_list)
    while count:
        print(next(iterator))
        count -= 1


input_list = input('Введите символы, разделенные пробелом: ').split()
repeats_count = input('Сколько раз повторить последовательность: ')
try:
    repeats_count = max(int(repeats_count),0)
except ValueError:
    print("Неверный ввод")
    exit()
repeate(input_list, repeats_count * len(input_list))
