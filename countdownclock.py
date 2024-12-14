'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

'''
Countdown Timer
-------------------------------------------------------------
'''


import time


def countdown(user_time):
   while user_time >= 0:
       mins, secs = divmod(user_time, 60)
       timer = '{:02d}:{:02d}'.format(mins, secs)
       print(timer, end='\r')
       time.sleep(1)
       user_time -= 1
   print('Lift off!')


if __name__ == '__main__':
   user_time = int(input("Enter a time in seconds: "))
   countdown(user_time)
   