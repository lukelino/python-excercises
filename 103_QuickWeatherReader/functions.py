"""Funkcje programu quickWeather"""

import pygal
from pygal import Config

# Konfiguracja wykresu
config = Config()
config.legend_at_bottom = True
config.interpolate = 'cubic'
config.y_title = 'Temperature'
config.x_title = 'Days'


def make_a_chart(y_min, y_max, x_hours, data_list, city, f_path):
    """Tworzy wykres i zapisuje w pliku svg"""
    line_chart = pygal.Line(legend_at_bottom=True, interpolate='cubic', y_title='Temperature', x_title='Days')
    line_chart.title = f'weather forecast for {city}'
    line_chart.x_labels = map(str, x_hours)  # map(str, range(1, 23, 3))
    for label, data_points in data_list:
        line_chart.add(label, data_points)
    # line_chart.add(final_clouds_list[0], final_clouds_list[1], secondary=True)       # Dodatkowa oś
    line_chart.range = [y_min, y_max]
    line_chart.render_to_file(f_path)
