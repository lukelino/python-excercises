#! python3
""" Otwiera stronę z argv[1] """
# www face --> www.facebook
# www yt --> you tube

import sys
import webbrowser

web_pages = {'face': 'https://www.facebook.com/', 'yt': 'https://www.youtube.com/?hl=pl&gl=PL'}
page = sys.argv[1]
if page in web_pages:
    webbrowser.open_new_tab(web_pages[page])
else:
    print('No page')
