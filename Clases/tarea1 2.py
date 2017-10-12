import time
import webbrowser

url = 'https://www.youtube.com/'
for r in range(0,3):
    print ("Loading a Youtube window")
    webbrowser.open(url)
    time.sleep(100)