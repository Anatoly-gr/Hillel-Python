# 5. Написать функцию square, принимающую 1 аргумент — сторону квадрата,
# и возвращающую 3 значения (с помощью кортежа): периметр квадрата,
# площадь квадрата и диагональ квадрата.
import math
def square(a):
    p = a * 2
    s = a ** 2
    d = math.sqrt(2) * a

