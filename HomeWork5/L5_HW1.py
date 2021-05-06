# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

stroka1 = input("Введите первую строку: ")
stroka2 = input("Введите вторую строку: ")
stroka3 = input("Введите третью строку: ")
str_list = [stroka1, stroka2, stroka3]
print(str_list)

with open("L5_zadanie1.txt", "w") as f_obj:
    f_obj.writelines("\n".join(str_list))