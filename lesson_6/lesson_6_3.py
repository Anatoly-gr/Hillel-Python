# 3. Дан список значений. Вернуть словарь где каждый ключ - это индекс списка,
#    а значение списка - это значение ключа:
#    Input:
# ['a', 'b', 'c', 'd', 'e']
#
#    Output
# {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'}
a = int()
some_list = list(x for x in 'abcde')
print(some_list)
index_list = []
for i in some_list:
    a = some_list.index(i)
    index_list.append(a)
print(index_list)

some_dict = {k: v for k, v in zip(index_list, some_list)}
print(some_dict)
