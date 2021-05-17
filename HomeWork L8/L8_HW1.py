# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        print(f"{self.day}-{self.month}-{self.year}")

    @classmethod
    def count(cls, day, month, year):
        my_list = []
        day = int(day)
        month = int(month)
        year = int(year)
        my_list.append(day)
        my_list.append(month)
        my_list.append(year)
        print(my_list)

    @staticmethod
    def check(day, month):
        if day > 31:
            print("Вы указали не верное число")
        if month > 12:
            print("Вы указали не верный месяц")

Data.count(2, 8, 1988)

