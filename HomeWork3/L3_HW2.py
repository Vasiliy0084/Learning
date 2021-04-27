# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

name = input("Введите Ваше имя: ")
surname = input("Введите вашу фамилию: ")
age = input("Год рождения: ")
city = input("Город: ")
email = input("Адрес электронной почты: ")
phone = input("Номер телефона: ")


def my_func(name, surname, age, city, email, phone) -> str:
    return f"{name}, {surname}, {age}, {city}, {email}, {phone}"


print(my_func(name, surname, age, city, email, phone))