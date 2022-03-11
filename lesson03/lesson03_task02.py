"""
2. Реализовать функцию, принимающую несколько параметров,
   описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
   Функция должна принимать параметры как именованные аргументы.
   Реализовать вывод данных о пользователе одной строкой.
"""


def user_info(name=None, female=None, year=None, city=None, email=None, phone=None):
    print(f"Имя: {name}, Фамилия: {female},  Год рождения: {year}, Город проживания: {city}, Email: {email}, Телефон: {phone}")


user_info(name='John', female='Smith', year=1986, city= 'New Yourk', email='john@yanoo.com', phone=4445644564)
