# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Stock:
    def __init__(self, art, name_org, model, quantity):
        self.art = art
        self.name_org = name_org
        self.model = model
        self.quantity = quantity

class Orgtech(Stock):
    def __init__(self, art, name_org, model, qyantity):
        super().__init__(art, name_org, model, qyantity)

class Printer(Orgtech):
    def __init__(self, art, name_org, model, color, print_type, print_color, quantity):
        self.art = art
        self.name_org = name_org
        self.model = model
        self.color = color
        self.print_type = print_type
        self.print_color = print_color
        self.quantity = quantity


class Scaner(Orgtech):
    def __init__(self, art, name_org, model, scan_color, quantity):
        self.art = art
        self.name_org = name_org
        self.model = model
        self.scan_color = scan_color
        self.quantity = quantity


class Xerox(Orgtech):
    def __init__(self, art, name, model, quantity):
        super().__init__(art, name, model, quantity)

samsung1 = Printer("A907341", "printer", "XP-900", 5)
print(samsung)