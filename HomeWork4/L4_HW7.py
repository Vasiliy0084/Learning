# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

number = int(input("Введите число: "))
n = list(range(1, number + 1))

from functools import reduce
result = reduce((lambda x, y: x * y), n)
print(result)

# Второй вариант
print("--------------------")


def fact():
    from math import factorial
    for el in {factorial(number)}:
        yield el

g = fact()
print(g)

for el in g:
    print(el)