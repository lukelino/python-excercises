#! python3
""" ściąga program telewizyjny dla EUROSPORTU i ELEVEN SPORTU ze strony teleman """

from bs4 import BeautifulSoup
import requests
import sys

# Początkowy URL strony 'teleman'
url = 'https://www.teleman.pl/'

user_channel = ''.join(sys.argv[1:])
tv_channels = {'euro1': 'eurosport', 'euro2': 'eurosport_2', 'eleven1': 'eleven', 'eleven2': 'eleven_sports'}

if user_channel in tv_channels.keys():
    address = f'https://www.telemagazyn.pl/{tv_channels[user_channel]}'
    res = requests.get(address)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, features='html.parser')
    # title = soup.find('div', class_='column').h1.text
    # print(title)
    for item in soup.find_all('li', class_='sport'):
        hour = item.em.text
        detail = item.find('a', class_='programInfo').span.text
        print(f'{hour} - {detail}')

