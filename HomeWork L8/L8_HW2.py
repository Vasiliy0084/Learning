# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class Exception:

    def func(self, arg1, arg2):
        try:
            print(arg1 / arg2)
        except ZeroDivisionError:
            print("На ноль делить нельзя")

rez = Exception()
rez.func(70, 0)
print(rez)