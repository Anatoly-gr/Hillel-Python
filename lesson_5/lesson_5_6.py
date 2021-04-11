# * доп. задание Написать функцию которая уберет из dict элементы с пустыми значениями:
#
#    {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
#    Должно вернуть {'first_color': 'Red', 'second_color': 'Green'} # * dict может быть произвольным
from typing import Optional, Dict


def remove_element(**def_dict):
    cng_dict = def_dict.copy()
    for key in cng_dict:
        if cng_dict[key] is None:
            cng_dict = def_dict.copy()
            del cng_dict[key]
    return cng_dict


some_dict = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
print(some_dict)
print(remove_element(**some_dict))
