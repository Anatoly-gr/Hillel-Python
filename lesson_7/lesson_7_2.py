# 2. Написать калькулятор температур.
#
# Пользователь вводит число и тип температуры (C, F, K - Цельсий, Фарренгейт, Кельвин соответственно)
# Программа должна вывести температуру в трех шкалах температур - Цельсий, Фарренгейт, Кельвин.

type_temperature = input('enter type of temperature: "C", "K", "F" ')
val_temperature = float(input('Input number of temperature: '))

if type_temperature == 'k' and val_temperature >= 0:
    print('Temperature C: ', val_temperature - 273.15)
    print('Temperature K: ', val_temperature)
    print('Temperature F: ', val_temperature - 459.67)

if type_temperature == 'c' and val_temperature + 273.15 >= 0:
    print('Temperature C: ', val_temperature)
    print('Temperature K: ', val_temperature + 273.15)
    print('Temperature F: ', val_temperature * 9 / 5 + 32)

if type_temperature == 'f' and val_temperature + 459.67 >= 0:
    print('Temperature C: ', (val_temperature - 32) * 5 / 9)
    print('Temperature K: ', (val_temperature - 32) * 5 / 9 + 273.15)
    print('Temperature F: ', val_temperature)
else:
    print('The temperature lower than absolute "zero"')
