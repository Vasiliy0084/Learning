# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open("L5_zadanie2.txt", "r") as f_obj:
    size = len([0 for _ in f_obj])
    print("Количество строк: ", size)

with open("L5_zadanie2.txt", "r") as f_ob:
    content = f_ob.readlines()
    print(content)
    for line in content:
        words = len(line.split())
        print("Количество слов в строке: ", words)