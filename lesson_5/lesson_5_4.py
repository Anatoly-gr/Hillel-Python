# 4. Дан список случайных целых чисел. Замените все нечетные числа списка нулями. И выведете их количество.
#
from random import randint

num_list = [randint(10, 100) for x in range(randint(10, 20))]
print(num_list)
