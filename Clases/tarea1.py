import time
import webbrowser

url = 'https://www.google.com'

def open_youtube(url):
    for r in range(0,3):
        print('Cargando ' + url)
        webbrowser.open(url)
        time.sleep(100)

open_youtube(url)

