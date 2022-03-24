"""
7. Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
"""

import functools
import json

with open("task07.txt", "r", encoding="utf-8") as file_obj:
    lines = file_obj.readlines()

profit = {name: float(income) - float(costs) for name, _, income, costs in [line.split() for line in lines]}
without_losses = [p for p in profit.values() if p >=0]
avg_profit = {"average_profit": functools.reduce(lambda x, y: x + y, without_losses) / len(without_losses)}
result = [profit, avg_profit]

with open("task07.json", "w") as write_f:
    json.dump(result, write_f)

print(result)
