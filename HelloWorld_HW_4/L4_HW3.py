#  Дан список заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут только уникальные элементы исходного.
#     Примечание. Списки создайте вручную, например так:
# my_list_1 = [2, 2, 5, 12, 8, 2, 12]
#
# В этом случае ответ будет:
# [5, 8]

my_list_1 = [2, 2, 5, 12, 8, 2, 12]
new_list = []
for i in my_list_1:
    if my_list_1.count(i) == 1:
        new_list.append(i)

print(new_list)