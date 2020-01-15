#! python3
"""
Skrypt pobierze ze schowka tekst i na początku każdego wiersza umieści gwiazdkę i spację, a następnie wstawi
tę listę do schowka.
"""
import pyperclip
text = pyperclip.paste()
print(text)
lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)
