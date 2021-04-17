# 1. Написать функцию которая вернет строку введенную пользователем.
#  Обернуть функцию в декоратор чтобы функция вместо строки целиком вернула список слов.
def some_deco(func):
    some_string = str(func())
    return print(some_string.split())


@some_deco
def str_func():
    return str(input('Input string: '))


str_func()
