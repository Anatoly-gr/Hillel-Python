# 4. Дан список:
#
# list_of_six = [100, 106, 112, 118, 124, 130, 136, 142, 148, 154, 160, 166, 172, 178, 184, 190, 196]
# Напечатать все числа которые делятся на 5 без остатка, но не больше 150.
#
list_of_six = [100, 106, 112, 118, 124, 130, 136, 142, 148, 154, 160, 166, 172, 178, 184, 190, 196]
print(list_of_six)
number_of_list = 0
for number_of_list in list_of_six:
    if number_of_list % 5 == 0 and number_of_list <= 150:
     print(number_of_list)
