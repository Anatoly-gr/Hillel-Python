# 2. Написать программу которая вернет количество введенных пользователем слов и общее число символов.
#
words = str(input("Введите несколько слов "))
new_list = words.split()
print('Количество введенных слов', len(new_list))
print('Количество введенных знаков ', words.count('') - 1)

