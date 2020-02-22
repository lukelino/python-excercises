#! python3
"""Sprawdzenie prognozy pogody"""

# Odczyt z wiersza poleceń lokalizacji
# Pobranie z witryny OpenWeatherMap.org danych prognozy w formacie JSON
# Konwersja JSON na strukturę Pythona
# Wyświetlenie prognozy

import json
import os
import sys
import requests
import pprint
import pygal
import datetime


if len(sys.argv) < 2:
    print('użycie: quickWeather lokalizacja')
    sys.exit()
location = ' '.join(sys.argv[1:])

url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid=ef47534ea6b531cafaa22020a088f8b2&units=metric'

response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)
# pprint.pprint(weatherData)
# pprint.pprint(weatherData.keys())

weather = weatherData['list']
city_name = weatherData['city']
days = dict(zip((1, 2, 3, 4, 5, 6, 7), ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')))

data_s = []

only_days_list = []
single_day = []
min_max = []
hours = []
for i in range(0, 39):
    timestamp = weather[i]['dt']
    dt = datetime.datetime.fromtimestamp(timestamp)
    date = dt.date()
    hour = dt.time()
    day = dt.isoweekday()

    # print(days[i], ' - ', city_name['name'], ' - ', weather[i]['dt'])
    # print(city_name['name'], ' - ', days[day],  ' - ', date, ', ', hour, day)
    # print(weather[i]['weather'][0]['main'], '-', weather[i]['weather'][0]['description'])
    # print('Temperature: '.ljust(5), weather[i]['main']['temp'], 'C')
    # print('Pressure: '.ljust(13), weather[i]['main']['pressure'], 'hPa')
    # print('Humidity: '.ljust(13), weather[i]['main']['humidity'], '%')
    # print()

    only_days_list.append(days[day])
    data_s.append(days[day])
    data_s.append(weather[i]['main']['temp'])
    min_max.append(weather[i]['main']['temp'])
    hours.append(hour)

# Utworzenie listy dni, dla których sprawdzana jest pogoda (pozbycie się duplikatów)
for s_day in only_days_list:
    if s_day not in single_day:
        single_day.append(s_day)

# Policzyć ilość wystąpień poszczególnych dni w głównej liście
single_day_occurrence = {}
for d in only_days_list:
    single_day_occurrence.setdefault(d, 0)
    single_day_occurrence[d] += 1

# Przygotowanie danych dla poszczególnych dni
final_list = []
len_of_tmp2 = 0

for i in range(len(single_day_occurrence)):
    iDay = data_s.index(single_day[i])
    tmp = data_s[iDay:iDay + single_day_occurrence[single_day[i]] * 2]  # Ile danych pobrać
    tmp2 = tmp[1::2]
    if i > 0:
        len_of_tmp2 += single_day_occurrence[single_day[i - 1]]
        for x in range(0, len_of_tmp2):
            tmp2.insert(0, None)   # Gwarantuje właściwe przesunięcie wykresu na osi czasu
    tmp4 = [single_day[i], tmp2]
    final_list.append(tmp4)

current_dir = r'D:\Py_repo\103_QuickWeatherReader'
filename = location + '.svg'
path = os.path.join(current_dir, filename)
print(f'File has been written as {path}')

# Wykres
line_chart = pygal.Line(legend_at_bottom=True)
line_chart.title = f'weather forecast for {location}'
line_chart.x_labels = map(str, hours)    # map(str, range(1, 23, 3))
for label, data_points in final_list:
    line_chart.add(label, data_points)
minimum = min(min_max) - 1      # Oś y
maximum = max(min_max) + 1      # Oś y
line_chart.range = [minimum, maximum]
line_chart.render_to_file(path)
