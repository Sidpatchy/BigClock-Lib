# Big Clock
import time
import threading

color = (255, 0, 0)

# minutes digit
def digitOne(number, color):
    print(number)
    return number

def digitTwo(number, color):
    print(number)
    return number

def digitThree(number, color):
    print(number)
    return number

def digitFour(number, color):
    print(number)
    return number
# Example
# digitOne(2, (255, 0 , 0))

num = 0

def firstDigit():
    global color
    global num
    digitOne(num, color)

def secondDigit():
    global color
    global num
    digitTwo(num, color)

def thirdDigit():
    global color
    global num
    digitThree(num, color)

def fourthDigit():
    global color
    global num
    digitFour(num, color)

try:
   t1 = threading.Thread(target=firstDigit, args=()) 
   t2 = threading.Thread(target=secondDigit, args=()) 
   t3 = threading.Thread(target=thirdDigit, args=()) 
   t4 = threading.Thread(target=fourthDigit, args=()) 
except:
   print('Error: unable to create thread')

iterations = 0

while iterations < 1000:
    try:
        t1 = threading.Thread(target=firstDigit, args=()) 
        t2 = threading.Thread(target=secondDigit, args=()) 
        t3 = threading.Thread(target=thirdDigit, args=()) 
        t4 = threading.Thread(target=fourthDigit, args=()) 
    except:
        print('Error: unable to create thread')
    try:
        t1.start()
        t2.start()
        t3.start()
        t4.start()
    except:
        print('Error: unable to start thread')

    try:
        t1.join()
        t2.join()
        t3.join()
        t4.join()
    except:
        print('Error: unable to join thread')

    if num >= 9:
        num = 0
    else:
        num = num + 1
    iterations = iterations + 1