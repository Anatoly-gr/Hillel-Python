# 4. Дан список случайных целых чисел. Замените все нечетные числа списка нулями. И выведете их количество.
#
from random import randint

num_list = [randint(10, 100) for x in range(randint(10, 20))]
print(num_list)
new_num_list = []

for num in num_list:
    if num % 2 == 0:
        num = 0
        new_num_list.append(num)
    else:
        new_num_list.append(num)
# print(num_list)
print(new_num_list)
print('Количество четных чисел ', new_num_list.count(0))
