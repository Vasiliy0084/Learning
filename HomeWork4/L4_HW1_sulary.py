# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

l_hours = int(input("Введите выработку в часах: "))
price = int(input("Укажите ставку рабочего часа: "))
profit = float(input("Укажите процент премии: "))


def sulary(l_hours, price, profit):
    result = (l_hours * price) + (l_hours * price) * profit
    return result


response = sulary(l_hours, price, profit)
print(response)