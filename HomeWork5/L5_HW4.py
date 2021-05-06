# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.


with open("L5_zadanie4.txt", "r") as f_obj:
    my_dict = {i.split("-")[0]: "-".join(i.replace("\n", "").split("-")[1:]) for i in f_obj}
    print(my_dict)
    print(my_dict.keys())
    new_dict = {"один": 1, "два": 2, "три": 3, "четыре": 4}
    my_dict.clear()
    my_dict.update(new_dict)
    print(my_dict)
    new_list = [my_dict]
    print(new_list)

with open("L5_zadanie4_res.txt", "w") as g_obj:
    g_obj.writelines(",".join(new_list))
