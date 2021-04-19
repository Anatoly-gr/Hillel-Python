# 3. Получить прогноз погоды для Одессы на следующие 5 дней и записать в файл с именем текущей даты,
import urllib.request
import json
from datetime import datetime

url = "http://api.openweathermap.org/data/2.5/forecast/daily?q=odesa&cnt=5&units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8"
request = urllib.request.urlopen(url)
data = json.load(request)
print(data)
new_list = data['list']
with open('19-04-2021-Odessa-5-days-weather-forecast.txt', 'r+') as file:
    for i in [0, 1, 2, 3, 4]:
        new_dict = new_list[i]
        dt_data = new_dict['dt']
        print(f'{datetime.fromtimestamp(dt_data).strftime("%d-%m-%Y")}, {new_dict["temp"]["day"]}, '
              f'{new_dict["temp"]["night"]}, {new_dict["feels_like"]["day"]}')
        file.write(f'\n {datetime.fromtimestamp(dt_data).strftime("%d-%m-%Y")}, {new_dict["temp"]["day"]}, '
                   f'{new_dict["temp"]["night"]}, {new_dict["feels_like"]["day"]}, \n')
