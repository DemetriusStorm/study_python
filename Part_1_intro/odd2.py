"""
04.04.2020
Part 1. odd.py
Print info if you current system time (minute) сcntaining in your odds list
'This minute seems a little odd' else 'Not an odd minute.'
"""

from datetime import datetime
import random
import time


# if you dont't want type this long list, comment off next line.
# odds = list(range(1, 60, 2))
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21,
        23, 25, 27, 29, 31, 33, 35, 37, 39, 41,
        43, 45, 47, 49, 51, 53, 55, 57, 59]

# time_now = datetime.today()  # Current time
# right_this_minute = time_now.minute
for i in range(5):
    wait_time = random.randint(1, 60)
    right_this_minute = datetime.today().minute

    if right_this_minute in odds:
        print('This minute seems a little odd, wait {} sec'.format(wait_time))
    else:
        print('Not an odd minute, wait {} sec'.format(wait_time))

    time.sleep(wait_time)
