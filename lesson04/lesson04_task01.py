"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
   В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
   Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv


def salary(hours, rate, bonus):
    return (hours*rate)+bonus


try:
    file, hours, rate, bonus = argv
    hours = int(hours)
    rate = float(rate)
    bonus = float(bonus)
except ValueError:
    print("Неверные аргументы")
    exit()
print(f"Итогова зарплата составит: {salary(hours, rate, bonus)}")

