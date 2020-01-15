#! python3
"""Test modułu requests"""

import requests

res = requests.get('http://gutenberg.org/files/27062/27062-0.txt')
try:
    res.raise_for_status()
    print(res.status_code)
    with open('Romeo_Julia.txt', 'wb') as f:
        for chunk in res.iter_content(100000):
            f.write(chunk)
except Exception as exc:
    print(f'Problem mamy: {exc}')
