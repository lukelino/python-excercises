""" Zgłaszanie wyjątku """
import logging
logging.basicConfig(filename='Error_logs.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)


def box_print(symbol, width, height):
    """Rysuje figurę z przekazanego symbolu"""
    if len(symbol) != 1:
        logging.debug('Symbol musi byc pojedynczym znakiem')
        raise Exception('Symbol musi byc pojedynczym znakiem')
    if width <= 2:
        logging.debug('Szerokość musi mieć wartość większą niż 2')
        raise Exception('Szerokość musi mieć wartość większą niż 2')
    if height <= 2:
        logging.debug('Wysokość musi mieć wartość większą niż 2')
        raise Exception('Wysokość musi mieć wartość większą niż 2')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


data = [('*', 4, 4), ('x', 10, 5), ('##', 6, 8), ('o', 1, 6), ('o', 10, 1)]

for values in data:
    try:
        box_print(*values)
    except Exception as err:
        print(f'Wyjątek: {err}')

logging.debug('Koniec programu')
