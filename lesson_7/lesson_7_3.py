# 3. Получить прогноз погоды для Одессы на следующие 5 дней и записать в файл с именем текущей даты,
import urllib.request
import json
from datetime import datetime
import requests

city = input('enter yor city: ')
num_day = int(input('enter number days: '))
api_id = 'f9ada9efec6a3934dad5f30068fdcbb8'
url = "http://api.openweathermap.org/data/2.5/forecast/daily?"
payload = {'q': city, 'cnt': num_day, 'units': 'metric', 'appid': api_id}
r = requests.get(url, params=payload)
request = urllib.request.urlopen(r.url)
data = json.load(request)
print(data)
new_list = data['list']
with open(f'19-04-2021-{city}-{num_day}-days-weather-forecast.txt', 'w') as file:
    file.write(f'Дата          Темп. днем   Темп. ночью   По ощущениям, \n')
    for i in range(num_day):
        new_dict = new_list[i]
        dt_data = new_dict['dt']
        file.write(f'{datetime.fromtimestamp(dt_data).strftime("%d-%m-%Y")},   {new_dict["temp"]["day"]}, '
                   f'       {new_dict["temp"]["night"]},        {new_dict["feels_like"]["day"]}, \n')
