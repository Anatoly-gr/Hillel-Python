# 3. Даны два целых числа `A` и `В`. Выведите все числа от `A` до `B` включительно,
# в порядке возрастания, если `A < B`, или в порядке убывания в противном случае.
number1 = int(input('Ведите первое число '))
number2 = int(input('Ведите второе число '))
som_list = list()
if number1 < number2:
    print(list(range(number1, number2 + 1)))
else:
    som_list = (list(range(number2, number1 + 1)))
    som_list.reverse()
    print(som_list)
