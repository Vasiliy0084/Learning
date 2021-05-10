# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"{self.title} Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print(f"{self.title} пишет чернилами")

class Pencil(Stationery):
    def draw(self):
        print(f"{self.title} карандаш рисует пока не сломается")

class Handle(Stationery):
    def draw(self):
        print(f"{self.title} выделяет текст")

parker = Pen("Parker")
print(parker.draw())

kohinor = Pencil("Koh-i-Nor")
print(kohinor.draw())

marker = Handle("Marker")
print(marker.draw())

pic = Stationery("Pic")
print(pic.draw())