# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

count_1 = int(input("Введите первое число: "))
count_2 = int(input("Введите второе число: "))
count_3 = int(input("Введите третье число: "))


def my_func(count_1, count_2, count_3):
    result = [count_1, count_2, count_3]
    result.remove(min(count_1, count_2, count_3))
    tot_1 = result[0]
    tot_2 = result[1]
    return tot_1 + tot_2


print("Сумма наибольших значений: ", my_func(count_1, count_2, count_3))