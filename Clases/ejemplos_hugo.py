"""
def get_sentence():
    return "The sum of {} and {} is {}"

def sumProblem(x, y):
    sum = x + y
    sentence = get_sentence().format(x, y, sum)
"""

import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program started on " + time.ctime())
while break_count < total_breaks:
    time.sleep(2)
    webbrowser.open_new("http://www.google.com")
    break_count = break_count + 1


