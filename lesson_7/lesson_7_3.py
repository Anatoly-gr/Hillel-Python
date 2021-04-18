# 3. Получить прогноз погоды для Одессы на следующие 5 дней и записать в файл с именем текущей даты,
import urllib.request
import json
from datetime import datetime

url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=odesa&cnt=5&units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8'
request = urllib.request.urlopen(url)
data = json.load(request)
print(data)
for
new_list = data['list']
for i in [0,1,2,3,4]:
    new_dict = new_list[i]
    print(new_dict['temp']['day'])
    dt_data = new_dict['dt']
    print(datetime.fromtimestamp(dt_data).strftime("%d-%m-%Y"))

