"""
4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
  speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
  которые должны сообщать, что машина поехала, остановилась, повернула (куда).
  Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
  Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
  Для классов TownCar и WorkCar переопределите метод show_speed.
  При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

  Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
  Выполните вызов методов и также покажите результат.
"""


class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        return f"Машина поехала со скростью {speed} км/ч"

    def stop(self):
        self.speed = 0
        return "Машина остановилась"

    def turn(self, direction):
        return f"Машина повернула {direction}"

    def show_speed(self):
        return f"Скорость автомобиля {self.name}: {self.speed} км/ч"


class TownCar(Car):
    max_speed = 60

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        result = f"Скорость автомобиля {self.name}: {self.speed} км/ч"
        return result if self.speed <= self.max_speed else result + f"\nПревышение скорости на {self.speed - self.max_speed} км/ч !!!"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    max_speed = 40

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        result = f"Скорость автомобиля {self.name}: {self.speed} км/ч"
        return result if self.speed <= self.max_speed else result + f"\nПревышение скорости на {self.speed - self.max_speed} км/ч !!!"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


audi = TownCar(65, 'Синяя', 'Audi A4', False)
ferrari = SportCar(150, 'Красная', 'Ferrari', False)
boxer = WorkCar(0, 'Белая', 'Peugeot Boxer', False)
skoda = PoliceCar(60, 'Серая', 'Skoda Octavia', True)

print(audi.turn("Направо"))
print(ferrari.turn("Налево"))
print(boxer.go(60))
print(skoda.stop())
print(audi.show_speed())
print(ferrari.show_speed())
print(boxer.show_speed())
print(skoda.show_speed())

print(f"{audi.color} машина {'полицеская' if audi.is_police else 'не полицеская'}")
print(f"{ferrari.color} {ferrari.name} едет со скоростью {ferrari.speed}")
print(f"{skoda.color} машина {'полицеская' if skoda.is_police else 'не полицеская'}")
print(f"{boxer.color} {boxer.name} едет со скоростью {boxer.speed}")