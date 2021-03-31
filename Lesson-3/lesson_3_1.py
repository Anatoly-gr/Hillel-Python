# 1. Пользователь вводит трехзначное число. Найдите сумму его цифр.
#
number = (input('Ведите трехзначное число '))
numbers = list(number)
print(numbers)
print(type(number))
for number in numbers:
    number = int(number)
    print(type(number))
