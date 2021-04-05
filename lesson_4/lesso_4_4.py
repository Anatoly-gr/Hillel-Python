# 4. По данному натуральному `n ≤ 9` выведите лесенку из `n` ступенек,
# `i`-я ступенька состоит из чисел от 1 до `i` без пробелов.
#
#    ```
#    1
#    12
#    123
#    1234
#    12345
#
from typing import List, Any

number = int(input('Ведите целое число от 1 до 9 '))
i = 1
k = int()
# some_list = list()
while i <= number + 1:
    some_list = list(range(1, i))
    numbers = ''.join(str(k) for k in some_list)
    print(numbers)
    i += 1
