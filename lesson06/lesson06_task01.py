"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
   Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
   красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
   второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
   Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
   Проверить работу примера, создав экземпляр и вызвав описанный метод.

   Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
   выводить соответствующее сообщение и завершать скрипт.
"""

from time import sleep
from itertools import cycle


class TrafficLight:
    __color: str
    __traffic_lights_timer = {"Красный": 7, "Желтый": 2, "Зеленый": 5}
    __colors_order = ["Красный", "Желтый", "Зеленый"]

    def __init__(self):
        self.__color = None

    def switch_light(self, next_color):
        current_color_order = self.__colors_order.index(self.__color) if self.__color is not None else -1
        if (self.__colors_order.index(next_color) - current_color_order == 1) or \
                (self.__colors_order.index(next_color) == 0 and current_color_order == len(self.__colors_order) - 1):
            self.__color = next_color
        else:
            print("В работе светофора произошел сбой.")
            exit(1)

    def running(self, seconds: int):
        lights = cycle(self.__traffic_lights_timer.keys())
        while True:
            self.switch_light(next(lights))
            print(f'{self.__color} будет гореть {self.__traffic_lights_timer.get(self.__color)} сек.')
            for i in range(self.__traffic_lights_timer.get(self.__color), 0, -1):
                if seconds <= 0:
                    print("Сфетофор завершил работу")
                    return
                seconds -= 1
                print(i)
                sleep(1)


break_time = input("На сколько секунд включить светофор? ")
try:
    break_time = int(break_time)
except ValueError:
    print("Неверный ввод")
    exit()
traffic_light = TrafficLight()
traffic_light.running(break_time)

#Проверка на контроль порядка переключения
traffic_light.switch_light("Зеленый")
