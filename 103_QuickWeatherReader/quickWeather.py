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

if len(sys.argv) < 2:
    print('użycie: quickWeather lokalizacja')
    sys.exit()
location = ' '.join(sys.argv[1:])

# url = f'http://api.openweathermap.org/data/2.5/forecast/daily?q=' \
#    f'{location}&cnt=7&APPID=0b0b27614262f706b53eb328f03b57fa&units=metric'
# url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&APPID=ef47534ea6b531cafaa22020a088f8b2'  #% location
url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid=ef47534ea6b531cafaa22020a088f8b2'

response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)
pprint.pprint(weatherData)
pprint.pprint(weatherData.keys())

weather = weatherData['list']
print(f'Aktualna pogoda w {location}')
print(weather[0]['weather'][0]['main'], '-', weather[0]['weather'][0]['description'])
print(weather[0]['main'][0]['pressure'], '-', weather[0]['weather'][0]['description'])
print()
print('Jutro:')
print(weather[1]['weather'][0]['main'], '-', weather[1]['weather'][0]['description'])
print()
print('Pojutrze:')
print(weather[2]['weather'][0]['main'], '-', weather[2]['weather'][0]['description'])
print()
