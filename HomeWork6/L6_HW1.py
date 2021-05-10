# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

class TrafficLight:
    trafficlight_color = 0

    def __init__(self, color, time):
        self.color = color
        self.time = time
        TrafficLight.trafficlight_color += 1

    def running(self):
        self.stop()
        self.wait()
        self.go()

    def stop(self):
        self.color = "red"
        self.time = 7
        print(self.color, "color light", self.time, "seconds")

    def wait(self):
        self.color = "yellow"
        self.time = 2
        print(self.color, "color light", self.time, "seconds")

    def go(self):
        self.color = "green"
        self.time = 15
        print(self.color, "color light", self.time, "seconds")

rezhim = TrafficLight("red", "7")
rezhim.running()
