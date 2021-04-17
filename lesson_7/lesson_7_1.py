# 1. Написать функцию которая вернет строку введенную пользователем.
#  Обернуть функцию в декоратор чтобы функция вместо строки целиком вернула список слов.
def some_deco(func):
    def wrapper():
        some_string = func()
        print(some_string.split(' '))

    return wrapper


@some_deco
def str_func():
    return str(input('Input string: '))


str_func()
