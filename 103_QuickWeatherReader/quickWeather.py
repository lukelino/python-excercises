#! python3
"""Sprawdzenie prognozy pogody"""

# Odczyt z wiersza poleceń lokalizacji
# Pobranie z witryny OpenWeatherMap.org danych prognozy w formacie JSON
# Konwersja JSON na strukturę Pythona
# Wyświetlenie prognozy

import json
import sys
import requests
import pprint
import pygal

if len(sys.argv) < 2:
    print('użycie: quickWeather lokalizacja')
    sys.exit()
location = ' '.join(sys.argv[1:])

# url = f'http://api.openweathermap.org/data/2.5/forecast/daily?q=' \
#    f'{location}&cnt=7&APPID=0b0b27614262f706b53eb328f03b57fa&units=metric'
# url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&APPID=ef47534ea6b531cafaa22020a088f8b2' % location
url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid=ef47534ea6b531cafaa22020a088f8b2&units=metric'
# url = f'http://pro.openweathermap.org/data/2.5/forecast/hourly?q={location}&appid=ef47534ea6b531cafaa22020a088f8b2'

response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)
# pprint.pprint(weatherData)
# pprint.pprint(weatherData.keys())

weather = weatherData['list']
city_name = weatherData['city']
# days = dict(zip((1, 2, 3), ('Now', 'Tomorrow', 'Day after tomorrow')))
days = list(range(1, 40))
data_s = []
data = []
for i in range(0, 39):

    print(days[i], ' - ', city_name['name'], ' - ', weather[i]['dt_txt'])
    print(weather[i]['weather'][0]['main'], '-', weather[i]['weather'][0]['description'])
    print('Temperature: '.ljust(5), weather[i]['main']['temp'], 'C')
    print('Pressure: '.ljust(13), weather[i]['main']['pressure'], 'hPa')
    print('Humidity: '.ljust(13), weather[i]['main']['humidity'], '%')
    print()
    data_s.append(str(weather[i]['dt_txt']))
    data_s.append(weather[i]['main']['temp'])
    data.append(data_s)
    data_s = []
    
print(data)
bar_chart = pygal.Bar()
bar_chart.title = f'weather forecast for {location}'
for label, data_points in data:
    bar_chart.add(label, data_points)
bar_chart.render_to_file(r'D:\Py_repo\103_QuickWeatherReader\temperature.svg')
