# 1. Написать функцию `is_prime`, принимающую 1 аргумент — число от 0 до 1000, и возвращающую `True`,
# если оно простое, и `False` - иначе.
#
# (Простые числа - те которые делятся без остатка только на само себя или 1, например 2, 3, 5, 7, 11...)
from math import sqrt


def is_prime(i):
    if i < 2:
        return False
    if i == 2:
        return True
    num = sqrt(i)
    k = 2
    while k <= num:
        if i % k == 0:
            return False
        k += 1
    return True


number = int(input('Введите целое число от 0 до 1000 '))
print(is_prime(number))
