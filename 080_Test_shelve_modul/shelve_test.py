#! python3
"""
    Test modułu shelve.
    Odczyt danych zapisanych w poprzednim projekcie.
"""
import shelve

data_file_path = r'F:\Py\079_Shelve_modul\data_file'

data = shelve.open(data_file_path)
print(list(data))
print('keys  -> ', list(data.keys()))
print('values ->', list(data.values()))
print(data['cats'], data['dogs'])

# dogs = ['Rocky', 'Nico', 'Lex']
# data['dogs'] = dogs

data.close()
