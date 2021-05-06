# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


with open("L5_zadanie3.txt", "r") as d_obj:
    my_dict = {i.split(" ")[0]: int(" ".join(i.replace("\n", "").split(" ")[1:])) for i in d_obj}
    print(my_dict)
    print(sum(my_dict.values()))
    people = {}
    for item in my_dict:
        if int(item) <= 20000
        print(my_dict, key)