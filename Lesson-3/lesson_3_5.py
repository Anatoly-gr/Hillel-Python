# 5. Пользователь вводит число от 1 до 10, программа генерирует рандомное число от 1 до 10,
# если числа равны напечатать 'You won!' если нет - 'You lose!'. Дать пользователю три попытки ;)
#
import random
i = 0
while i < 3:
    rnd = random.randint(0, 11)
    "print(rnd)"
    user_number = int(input('Введите целое число от 1 до 10 '))
    if user_number == rnd:
        print('Congratulations You Won!!!')
    else:
        print('Sorry you louse')
    i = i + 1
