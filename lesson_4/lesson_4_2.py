# 2. Программа запрашивает ввод последовательности целых неотрицательных чисел, пока не будет введён 0.
# Как только будет введён 0 (ноль), программа должна посчитать и вывести на экран:
#
# - количество введённых чисел (завершающий 0 не считается)
#
# - их сумму
#
# - произведение
#
# - среднее арифметическое (не считая завершающего числа 0)
#
# - определить значение и порядковый номер наибольшего элемента последовательности.
# Если наибольших элементов несколько, выведите порядковый номер первого из них.
#
# - определить количество чётных и не чётных элементов в последовательности
#
# - определить значение второго по величине элемента в этой последовательности
#
# - определите, сколько элементов этой последовательности равны ее наибольшему элементу


import functools
import operator

some_number = int(input("введите целое число "))
some_list = list()
some_list.append(some_number)
while some_number != 0:
    some_number = int(input("введите еще целое число "))
    some_list.append(some_number)
#    print(some_number)
some_list.remove(-0)
print(some_list)
print('Количество введенных чисел ', len(some_list))
print('сумма введенных чисел = ', sum(some_list))
print('произведение введенных чисел = ', functools.reduce(operator.mul, some_list))
print('средне арифметическое значение введенных чисел = ', sum(some_list) / len(some_list))
print('Значение максимального элемента = ', max(some_list), 'Индекс максимального элемента',
      some_list.index(max(some_list)))
print('Кол-во элементов последовательности равных максимальному элементу ', some_list.count(max(some_list)))
new_list = list()
for element in some_list:
    if element % 2 == 0:
        new_list.append(element)
print('Количество четных элементов списка', len(new_list))
print('Количество нечетных элементов списка', len(some_list) - len(new_list))
second_max = int(0)
i = 0
for i in some_list:
    if max(some_list) > i >= second_max:
        second_max = i
print('Значение второго по величине элемента = ', second_max)
