# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Автомобиль {self.name}, {self.color} цвета поехал со скоростью {self.speed} км.ч")

    def stop(self):
        print(f"Автомобиль {self.name}, {self.color} цвета остановился")

    def turn(self):
        print(f"Автомобиль {self.name}, {self.color} цвета повернул")

    def show_speed(self):
        print(f"{self.name} скорость в пределах допуска")

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super(TownCar, self).__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print("Привышение установленной скорости")
        else:
            print(f"{self.name} скорость в пределах допуска")

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super(SportCar, self).__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super(WorkCar, self).__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print("Привышение установленной скорости")
        else:
            print(f"{self.name} скорость в пределах допуска")

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super(PoliceCar, self).__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Автомобиль {self.name} принадлежит полиции, может ехать с любой скоростью")


lada = TownCar(70, "white", "Priora", "not police")
print(lada.go())
print((lada.stop()))
print(lada.turn())
print(lada.show_speed())

ferrary = SportCar(130, "red", "Enzo", "not police")
print(ferrary.go())
print(ferrary.show_speed())
print(ferrary.stop())

gazel = WorkCar(30, "white", "GAZ 3302", "not police")
print((gazel.go()))
print(gazel.show_speed())
print(gazel.turn())

ford = PoliceCar(150, "yellow", "focus", "police")
print(ford.go())
print(ford.show_speed())
print(ford.stop())