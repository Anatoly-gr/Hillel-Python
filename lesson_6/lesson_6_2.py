# 2. Написать функцию которая возвращает текущее время.
# И обернуть ее в декоратор @countdown
#     который отсчитает 3 секунды.
#
#    Пример:
# #    >>> what_time_is_it_now()
#    3
#    2
#    1
#    '16:21'
#
# time.sleep() поможет программе уснуть на первый аргумент секунду =)
# #    Вернуть время поможет метод time.strftime, с аргументом '%H:%M'
import time
from datetime import datetime


def count_down(func):
    for i in [1, 2, 3]:
        time.sleep(1)
        print(4-i)
    return func


@count_down
def what_time_is_now():
    a = datetime.now().time()
    print(a.strftime('%H:%M'))


what_time_is_now()
