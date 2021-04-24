# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

list = input("Введите фразу: ")
fraze = list.split()
count = len(fraze)
number = 0
while number < count:
    word = fraze[0 + number]
    print(number + 1, word[:10])
    number = number + 1