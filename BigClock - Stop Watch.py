# Big Clock
import board
import neopixel
import time
import displayDriver as dis
import threading

startTime = time.time()

pixels = neopixel.NeoPixel(board.D18, 86)
color = (100, 0, 0)
# Example
# dis.digitOne(2, (255, 0 , 0))

digit1 = 0
digit2 = 0
digit3 = 0
digit4 = 0

dis.digitOne(digit1, color)
dis.digitTwo(digit2, color)
dis.digitThree(digit3, color)
dis.digitFour(digit4, color)

pixels[42] = color
pixels[43] = color

number = 0

while True:

    number = number + 1
    string = [int(i) for i in str(number)]
    print(string)

    if number <= 9:
        digit1 = (string[0])
    elif number > 9:
        brainCellsExist = list(reversed(string))
        digit2 = (brainCellsExist[1])
        digit1 = (brainCellsExist[0])

    if digit2 >= 6:
            digit2 = 0
            digit3 = digit3 + 1
            if digit3 >= 9:
                digit3 = 0
                digit4 = digit4 + 1
                if digit4 >= 9:
                    digit1 = 0
                    digit2 = 0
                    digit3 = 0
                    digit4 = 0

    if number >= 59:
        number = 0
        digit1 = 0
        digit2 = 0
        if digit3 > 9:
            digit4 = digit4 + 1
            digit3 = 0
        else:
            digit3 = digit3 + 1

    try:
       t1 = threading.Thread(target=dis.digitOne, args=(digit1, color))
       t2 = threading.Thread(target=dis.digitTwo, args=(digit2, color))
       t3 = threading.Thread(target=dis.digitThree, args=(digit3, color))
       t4 = threading.Thread(target=dis.digitFour, args=(digit4, color))
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

    if number >= 59:
        number = 0

    time.sleep(1 - ((time.time() - startTime) % 1))
