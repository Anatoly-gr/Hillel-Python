# 2. Пользователь вводит действительное (вещественное) число `X`, которое имеет два знака после десятичной точки.
#
#    - Выведите его дробную часть.
#
#    - Выведите его первую цифру после десятичной точки.
import math

number = float(input('Введите число с двумя знаками после запятой '))
kort = math.modf(number)
drob = str(round(kort[0], 2))
print('дробная часть введеного числа ',  drob)
somelist = list(drob)
print('Первая цифра после десятичной точки ', list(drob)[2])

# print(a_tuple)
# numbers = tuple(number)
# print(numbers(split()))