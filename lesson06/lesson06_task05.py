"""
5. Реализовать класс Stationery (канцелярская принадлежность).
   Определить в нем атрибут title (название) и метод draw (отрисовка).
   Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
   Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
   Для каждого из классов метод должен выводить уникальное сообщение.
   Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationary:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationary):
    def draw(self):
        print(f'Запуск отрисовки ручкой')


class Pencil(Stationary):
    def draw(self):
        print(f'Запуск отрисовки карандашом')


class Handle(Stationary):
    def draw(self):
        print(f'Запуск отрисовки маркером')


stationary = Stationary("Канцелярия")
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

print(stationary.title+":")
stationary.draw()
print(pen.title+":")
pen.draw()
print(pencil.title+":")
pencil.draw()
print(handle.title+":")
handle.draw()
