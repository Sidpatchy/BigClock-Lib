# Big Clock
import board
import neopixel
import time
import displayDriver as dis

pixels = neopixel.NeoPixel(board.D18, 86)

# Example
# dis.digitOne(2, (255, 0 , 0))

digit1 = 0
digit2 = 0
digit3 = 0
digit4 = 0

digitOne(digit1, (255, 0, 0))
digitTwo(digit2, (255, 0, 0))
digitThree(digit3, (255, 0, 0))
digitFour(digit4, (255, 0, 0))

number = 0

while True:
    pixels[42] = (255, 0 , 0)
    pixels[43] = (255, 0 , 0)

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

    dis.digitOne(digit1, (255, 0, 0))
    dis.digitTwo(digit2, (255, 0, 0))
    dis.digitThree(digit3, (255, 0, 0))
    dis.digitFour(digit4, (255, 0, 0))
    
    if number >= 59:
        number = 0

    time.sleep(.51)