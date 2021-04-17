# 2. Написать калькулятор температур.
#
# Пользователь вводит число и тип температуры (C, F, K - Цельсий, Фарренгейт, Кельвин соответственно)
# Программа должна вывести температуру в трех шкалах температур - Цельсий, Фарренгейт, Кельвин.

type_temperature = input('enter type of temperature: "C", "K", "F" ')
val_temperature = int(input('Input number of temperature: '))
temp_dict = {'k': val_temperature, 'c': val_temperature, 'f': val_temperature}
# print(temp_dict)
if type_temperature == 'k' and val_temperature < 0:
    print("значение температуры не может быть меньше нуля")

if type_temperature == 'k':
    temp_dict = {'k': val_temperature, 'c': val_temperature - 273.15, 'f': val_temperature - 459.67}
    print('Temperature C: ', temp_dict['c'])
    print('Temperature K: ', temp_dict['k'])
    print('Temperature F: ', temp_dict['f'])
if type_temperature == 'c':
    temp_dict = {'k': val_temperature + 273.15, 'c': val_temperature,
                 'f': val_temperature * 9 / 5 + 32}
    print('Temperature C: ', temp_dict['c'])
    print('Temperature K: ', temp_dict['k'])
    print('Temperature F: ', temp_dict['f'])
if type_temperature == 'f':
    temp_dict = {'k': (val_temperature - 32) * 5 / 9 + 273.15,
                 'c': (val_temperature - 32) * 5 / 9, 'f': val_temperature}
    print('Temperature C: ', temp_dict['c'])
    print('Temperature K: ', temp_dict['k'])
    print('Temperature F: ', temp_dict['f'])
