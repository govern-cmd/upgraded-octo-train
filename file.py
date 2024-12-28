import time

def countdown(t: int):             # Create function with the parameter of t 
    while t > 0:                   # Inside function
        print(f'Time remaining: {t}')  # f-string with the variable t
        time.sleep(1)              # Put the program to sleep for 1 second
        t -= 1
    print('Timer reached 0!')      # This line is outside the while loop

countdown(10)


