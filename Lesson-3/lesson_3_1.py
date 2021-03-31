# 1. Пользователь вводит трехзначное число. Найдите сумму его цифр.
#
number = (input('Ведите число '))
numbers = list(number)
some_list = []
# print(numbers)
# print(type(number))
for number in numbers:
    number = int(number)
    some_list.append(number)
    # print(type(number))
print('сумма цифр введеного числа ', sum(some_list))
