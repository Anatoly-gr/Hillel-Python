# 1. Написать функцию которая вернет строку введенную пользователем.
#  Обернуть функцию в декоратор чтобы функция вместо строки целиком вернула список слов.
# def some_deco(*func):
#     print(func)
#
#
# @some_deco"
def str_func():
    som_lst = str(input('Input string: '))
    print(som_lst.split(' '))


str_func()
