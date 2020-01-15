#! python3
import pprint

cats = [{'name': 'Morpheus', 'age': 42}, {'name': 'Heroin', 'age': 41}, {'name': 'Too Tight', 'age': 33}]
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()
