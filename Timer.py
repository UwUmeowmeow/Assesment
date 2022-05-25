import time
import datetime


mode = input("What difficulty are you choosing easy or hard: ")

def countdown(s):


    total_seconds = s


    while total_seconds > 0:

        if mode =

            timer = datetime.timedelta(seconds = total_seconds)


            print(timer, end="\r")

            # Delays the program one second
            time.sleep(1)

            # Reduces total time by one second
            total_seconds -= 1

        else mode = easy:



    print("Bzzzt! The countdown is at zero seconds!")



# Inputs for hours, minutes, seconds on timer

s = input(f" {mode}")
countdown(int(s))
