# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open("L5_zadanie5.txt", "w") as f_obj:
    number_list = ("1 3 4 17 80 90 57 145 324")
    f_obj.writelines(number_list)

with open("L5_zadanie5.txt", "r") as d_obj:
    cont = d_obj.readlines()
    cont = cont[0].split(" ")
    count = [int(x) for x in cont]
    result = sum(count)

with open("L5_zadanie5.txt", "a") as c_obj:
    print("\nСумма указанных чисел равняется: ", result, file=c_obj)