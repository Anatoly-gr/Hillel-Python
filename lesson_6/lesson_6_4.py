# 4. Во вложении есть json файл. Написать программу которая прочитает его
# и посчитает общую длительность всех треков в альбоме.
#
# Базовый кейс - вернет количество секунд.
#    * доп. усложнение вернуть в виде строки часы:минуты:секунды,
#    прим. '0:41:39' (datetime.timedelta)
import json

with open('acdc.json', 'r+') as file:
    some_dict = (json.load(file))
some_dict_tracks = (some_dict['album']['tracks'])  # извлечение первого элемента со списка
list_tracks = some_dict_tracks['track']
print(list_tracks)
# print(type(list_tracks))
# print(len(list_tracks))
dur = []
for track in list_tracks:
    # print(type(track))
    for key in track:
        if key == 'duration':
            track[key] = int(track[key])
            dur.append(track[key])
print('длина треков', sum(dur))
