"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
   В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
   и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
   месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date_str: str):
        self.date_str = date_str

    @classmethod
    def str_to_int(cls, date_str):
        result = [int(x) for x in date_str.split("-")]
        if Date.validate(*result):
            return result
        else:
            raise ValueError("Не верный формат даты")

    @staticmethod
    def validate(d, m, y):
        return True if (1 <= d <= 31) and (1 <= m <= 12) and (1 <= y <= 9999) else None


date1 = "12-04-2022"
day, month, year = Date.str_to_int(date1)
print(f"{day:>02}/{month:>02}/{year:>04}")

date2="01-01-1999"
date_obj = Date(date2)
day, month, year = date_obj.str_to_int(date2)
print(f"{day:>02}/{month:>02}/{year:>04}")
