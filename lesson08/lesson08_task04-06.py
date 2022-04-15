"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
   который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
   В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
   уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
   передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц
   оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
   Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
   Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
   изученных на уроках по ООП.
"""


class StorageError(Exception):
    def __init__(self, txt):
        self.txt = txt


class OfficeEquipment:
    vendor: str
    model: str

    def __init__(self, vendor, model):
        self.vendor = vendor
        self.model = model

    def __str__(self):
        return f"{self.vendor} {self.model}"


class Storage:
    capacity: int
    name: str

    def __init__(self, name: str, capacity: int):
        self.capacity = capacity
        self.name = name
        self.stock = {}

    def put(self, equipment: OfficeEquipment, quantity: int):
        #Добавляем модель устройства и количество
        try:
            if sum(self.stock.values()) + quantity <= self.capacity:
                if self.stock.get(equipment.model) is None:
                    self.stock.setdefault(equipment.model, quantity)
                else:
                    self.stock.update({equipment.model: quantity + self.stock.get(equipment.model)})
            else:
                raise StorageError(
                    f"На складе {self.name} недостаточно свободного места. Доступно {self.capacity - sum(self.stock.values())}")
        except StorageError as err:
            print(err)

    def get(self, equipment: OfficeEquipment, quantity: int):
        # Извлекаем со склада по названию модели
        quantity_on_stock = self.stock.get(equipment.model) if self.stock.get(equipment.model) is not None else 0
        try:
            if quantity_on_stock >= quantity:
                self.stock.update({equipment.model: quantity_on_stock - quantity})
            else:
                raise StorageError(f"Остатка {equipment.model} на складе {self.name} недостаточно")
        except StorageError as err:
            print(err)

    @staticmethod
    def move(old_storage, new_storage, equipment: OfficeEquipment, quantity: int):
        if not(isinstance(old_storage, Storage) and isinstance(new_storage, Storage)):
            raise TypeError(f"В метод переданы элементы не соответвующего класса")
        quantity_on_stock = old_storage.stock.get(equipment.model) if old_storage.stock.get(equipment.model) is not None else 0
        try:
            if quantity_on_stock < quantity:
                raise StorageError(f"Остатка {equipment.model} на складе {old_storage.name} недостаточно")
            elif sum(new_storage.stock.values()) + quantity > new_storage.capacity:
                raise StorageError(
                    f"На складе {new_storage.name} недостаточно свободного места. Доступно {new_storage.capacity - sum(new_storage.stock.values())}")
            else:
                old_storage.get(equipment, quantity)
                new_storage.put(equipment, quantity)
        except StorageError as err:
            print(err)

    @staticmethod
    def validate_qty(quantity):
        try:
            return int(quantity)
        except ValueError:
            print(f"Переданное количество {quantity} не является числом!")
            exit(1)


class Printer(OfficeEquipment):
    print_speed: int #листов в минуту
    color_print: bool #цветная печать

    def __init__(self, vendor, model, print_speed, color_print):
        super().__init__(vendor, model)
        self.print_speed = print_speed
        self.color_print = color_print

    def __str__(self):
        return f"{self.vendor} {self.model} {self.print_speed} л/мин, {'Цветной' if self.color_print else 'Ч/Б'}"


class Scanner(OfficeEquipment):
    scan_speed: int #секунд на 1 сканирование
    resolution: int #качестdо сканирования в dpi

    def __init__(self, vendor, model, scan_speed, resolution):
        super().__init__(vendor, model)
        self.scan_speed = scan_speed
        self.resolution = resolution

    def __str__(self):
        return f"{self.vendor} {self.model} {self.scan_speed} сек, {self.resolution} dpi"


class Copier(OfficeEquipment):
    copy_speed: int #листов в минуту
    color_copy: bool #цветная копия
    resolution: int  # качество копии в dpi

    def __init__(self, vendor, model, copy_speed, color_copy, resolution):
        super().__init__(vendor, model)
        self.copy_speed = copy_speed
        self.color_copy = color_copy
        self.resolution = resolution

    def __str__(self):
        return f"{self.vendor} {self.model} {self.copy_speed} л/мин, {'Цветной' if self.color_copy else 'Ч/Б'}, {self.resolution} dpi"


#Создаем экзмпляры оргтехники
p1 = Printer("HP", "LJ1215", 10, False)
s1 = Scanner("Canon", "LIDE 220", 29, 200)
cp1 = Copier("Xerox", "B205", 5, True, 150)
print(p1)
print(s1)
print(cp1)

#Размещаем оргтехнику на складе
storage = Storage("Склад 1", 10)
department = Storage("Подразделение 1", 5)
storage.put(p1, 5)
storage.put(s1, 2)
storage.put(cp1, 1)

print("\nСостояние складов:")
print(storage.name, storage.stock)
print(department.name, department.stock)

#Перемещаем принтеры и проверяем работу
input_qty = Storage.validate_qty(input("Сколько принтеров отправить со склада в подразделение? \n>>>> "))
Storage.move(storage, department, p1, input_qty)
print("\nСостояние складов после перемещения:")
print(storage.name, storage.stock)
print(department.name, department.stock)

