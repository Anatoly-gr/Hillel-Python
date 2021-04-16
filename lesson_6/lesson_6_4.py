# 4. Во вложении есть json файл. Написать программу которая прочитает его
# и посчитает общую длительность всех треков в альбоме.
#
# Базовый кейс - вернет количество секунд.
#    * доп. усложнение вернуть в виде строки часы:минуты:секунды,
#    прим. '0:41:39' (datetime.timedelta)
import datetime
import json

with open('acdc.json', 'r+') as file:
    some_dict = (json.load(file))
    durations = some_dict['album']['tracks']['track']  # извлечение первого элемента со списка
    dur = [int(duration['duration']) for duration in durations]
    print(sum(dur))

print(datetime.timedelta(0, sum(dur)))
