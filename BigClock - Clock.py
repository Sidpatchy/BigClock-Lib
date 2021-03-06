# Big Clock
import board
import neopixel
import time
import datetime

brightness = (10, 0, 0)
off = (255, 255, 255)

pixels = neopixel.NeoPixel(board.D18, 86)

# minutes
def digitOne(number, color):
    display = number
    global off
    if display == 0:
        pixels[5] = (color)
        pixels[4] = (color)
        pixels[3] = (color)
        pixels[2] = (color)
        pixels[1] = (color)
        pixels[0] = (color)
        pixels[6] = (color)
        pixels[7] = (color)
        pixels[8] = (color)
        pixels[9] = (color)
        pixels[10] = (color)
        pixels[11] = (color)
        pixels[12] = (color)
        pixels[13] = (color)
        pixels[14] = (color)
        pixels[15] = (color)
        pixels[16] = (color)
        pixels[17] = (color)
        pixels[20] = (off)
        pixels[19] = (off)
        pixels[18] = (off)
        pixels.show()
        
    elif display == 1:
        pixels[0] = (color)
        pixels[1] = (color)
        pixels[2] = (color)
        pixels[15] = (color)
        pixels[16] = (color)
        pixels[17] = (color)
        pixels[5] = (off)
        pixels[4] = (off)
        pixels[3] = (off)
        pixels[6] = (off)
        pixels[7] = (off)
        pixels[8] = (off)
        pixels[20] = (off)
        pixels[19] = (off)
        pixels[18] = (off)
        pixels[9] = (off)
        pixels[10] = (off)
        pixels[11] = (off)
        pixels[12] = (off)
        pixels[13] = (off)
        pixels[14] = (off)
        pixels.show()
        
    elif display == 2:
        pixels[5] = (color)
        pixels[4] = (color)
        pixels[3] = (color)
        pixels[2] = (color)
        pixels[1] = (color)
        pixels[0] = (color)
        pixels[18] = (color)
        pixels[19] = (color)
        pixels[20] = (color)
        pixels[9] = (color)
        pixels[10] = (color)
        pixels[11] = (color)
        pixels[12] = (color)
        pixels[13] = (color)
        pixels[14] = (color)
        pixels[6] = (off)
        pixels[7] = (off)
        pixels[8] = (off)
        pixels[17] = (off)
        pixels[16] = (off)
        pixels[15] = (off)
        pixels.show()

    elif display == 3:
        pixels[5] = (color)
        pixels[4] = (color)
        pixels[3] = (color)
        pixels[2] = (color)
        pixels[1] = (color)
        pixels[0] = (color)
        pixels[20] = (color)
        pixels[19] = (color)
        pixels[18] = (color)
        pixels[17] = (color)
        pixels[16] = (color)
        pixels[15] = (color)
        pixels[14] = (color)
        pixels[13] = (color)
        pixels[12] = (color)
        pixels[6] = (off)
        pixels[7] = (off)
        pixels[8] = (off)
        pixels[9] = (off)
        pixels[10] = (off)
        pixels[11] = (off)
        pixels.show()
        
    elif display == 4:
        pixels[6] = (color)
        pixels[7] = (color)
        pixels[8] = (color)
        pixels[20] = (color)
        pixels[19] = (color)
        pixels[18] = (color)
        pixels[2] = (color)
        pixels[1] = (color)
        pixels[0] = (color)
        pixels[17] = (color)
        pixels[16] = (color)
        pixels[15] = (color)
        pixels[5] = (off)
        pixels[4] = (off)
        pixels[3] = (off)
        pixels[9] = (off)
        pixels[10] = (off)
        pixels[11] = (off)
        pixels[12] = (off)
        pixels[13] = (off)
        pixels[14] = (off)
        pixels.show()

    elif display == 5:
        pixels[3] = (color)
        pixels[4] = (color)
        pixels[5] = (color)
        pixels[6] = (color)
        pixels[7] = (color)
        pixels[8] = (color)
        pixels[20] = (color)
        pixels[19] = (color)
        pixels[18] = (color)
        pixels[17] = (color)
        pixels[16] = (color)
        pixels[15] = (color)
        pixels[14] = (color)
        pixels[13] = (color)
        pixels[12] = (color)
        pixels[2] = (off)
        pixels[1] = (off)
        pixels[0] = (off)
        pixels[9] = (off)
        pixels[10] = (off)
        pixels[11] = (off)
        pixels.show()

    elif display == 6:
        pixels[5] = (color)
        pixels[4] = (color)
        pixels[3] = (color)
        pixels[6] = (color)
        pixels[7] = (color)
        pixels[8] = (color)
        pixels[20] = (color)
        pixels[19] = (color)
        pixels[18] = (color)
        pixels[17] = (color)
        pixels[16] = (color)
        pixels[15] = (color)
        pixels[14] = (color)
        pixels[13] = (color)
        pixels[12] = (color)
        pixels[11] = (color)
        pixels[10] = (color)
        pixels[9] = (color)
        pixels[2] = (off)
        pixels[1] = (off)
        pixels[0] = (off)
        pixels.show()

    elif display == 7:
        pixels[5] = (color)
        pixels[4] = (color)
        pixels[3] = (color)
        pixels[2] = (color)
        pixels[1] = (color)
        pixels[0] = (color)
        pixels[17] = (color)
        pixels[16] = (color)
        pixels[15] = (color)
        pixels[6] = (off)
        pixels[7] = (off)
        pixels[8] = (off)
        pixels[20] = (off)
        pixels[19] = (off)
        pixels[18] = (off)
        pixels[9] = (off)
        pixels[10] = (off)
        pixels[11] = (off)
        pixels[12] = (off)
        pixels[13] = (off)
        pixels[14] = (off)
        pixels.show()

    elif display == 8:
        pixels[5] = (color)
        pixels[4] = (color)
        pixels[3] = (color)
        pixels[2] = (color)
        pixels[1] = (color)
        pixels[0] = (color)
        pixels[6] = (color)
        pixels[7] = (color)
        pixels[8] = (color)
        pixels[20] = (color)
        pixels[19] = (color)
        pixels[18] = (color)
        pixels[9] = (color)
        pixels[10] = (color)
        pixels[11] = (color)
        pixels[12] = (color)
        pixels[13] = (color)
        pixels[14] = (color)
        pixels[15] = (color)
        pixels[16] = (color)
        pixels[17] = (color)
        pixels.show()

    elif display == 9:
        pixels[5] = (color)
        pixels[4] = (color)
        pixels[3] = (color)
        pixels[2] = (color)
        pixels[1] = (color)
        pixels[0] = (color)
        pixels[6] = (color)
        pixels[7] = (color)
        pixels[8] = (color)
        pixels[20] = (color)
        pixels[19] = (color)
        pixels[18] = (color)
        pixels[12] = (color)
        pixels[13] = (color)
        pixels[14] = (color)
        pixels[15] = (color)
        pixels[16] = (color)
        pixels[17] = (color)
        pixels[9] = (off)
        pixels[10] = (off)
        pixels[11] = (off)
        pixels.show()

# minutes again
def digitTwo(number, color):   
    if number == 0:
        pixels[26] = (color)
        pixels[25] = (color)
        pixels[24] = (color)
        pixels[23] = (color)
        pixels[22] = (color)
        pixels[21] = (color)
        pixels[33] = (color)
        pixels[34] = (color)
        pixels[35] = (color)
        pixels[36] = (color)
        pixels[37] = (color)
        pixels[38] = (color)
        pixels[39] = (color)
        pixels[40] = (color)
        pixels[41] = (color)
        pixels[29] = (color)
        pixels[28] = (color)
        pixels[27] = (color)
        pixels[30] = (off)
        pixels[31] = (off)
        pixels[32] = (off)
        pixels.show()

    elif number == 1:
        pixels[23] = (color)
        pixels[22] = (color)
        pixels[21] = (color)
        pixels[33] = (color)
        pixels[34] = (color)
        pixels[35] = (color)
        pixels[24] = (off)
        pixels[25] = (off)
        pixels[26] = (off)
        pixels[27] = (off)
        pixels[28] = (off)
        pixels[29] = (off)
        pixels[30] = (off)
        pixels[31] = (off)
        pixels[32] = (off)
        pixels[41] = (off)
        pixels[40] = (off)
        pixels[39] = (off)
        pixels[38] = (off)
        pixels[37] = (off)
        pixels[36] = (off)
        pixels.show()

    elif number == 2:
        pixels[26] = (color)
        pixels[25] = (color)
        pixels[24] = (color)
        pixels[23] = (color)
        pixels[22] = (color)
        pixels[21] = (color)
        pixels[32] = (color)
        pixels[31] = (color)
        pixels[30] = (color)
        pixels[41] = (color)
        pixels[40] = (color)
        pixels[39] = (color)
        pixels[38] = (color)
        pixels[37] = (color)
        pixels[36] = (color)
        pixels[27] = (off)
        pixels[28] = (off)
        pixels[29] = (off)
        pixels[33] = (off)
        pixels[34] = (off)
        pixels[35] = (off)
        pixels.show()
    
    elif number == 3:
        pixels[26] = (color)
        pixels[25] = (color)
        pixels[24] = (color)
        pixels[23] = (color)
        pixels[22] = (color)
        pixels[21] = (color)
        pixels[30] = (color)
        pixels[31] = (color)
        pixels[32] = (color)
        pixels[33] = (color)
        pixels[34] = (color)
        pixels[35] = (color)
        pixels[36] = (color)
        pixels[37] = (color)
        pixels[38] = (color)
        pixels[27] = (off)
        pixels[28] = (off)
        pixels[29] = (off)
        pixels[41] = (off)
        pixels[40] = (off)
        pixels[39] = (off)
        pixels.show()
    
    elif number == 4:
        pixels[27] = (color)
        pixels[28] = (color)
        pixels[29] = (color)
        pixels[30] = (color)
        pixels[31] = (color)
        pixels[32] = (color)
        pixels[23] = (color)
        pixels[22] = (color)
        pixels[21] = (color)
        pixels[33] = (color)
        pixels[34] = (color)
        pixels[35] = (color)
        pixels[26] = (off)
        pixels[25] = (off)
        pixels[24] = (off)
        pixels[41] = (off)
        pixels[40] = (off)
        pixels[39] = (off)
        pixels[38] = (off)
        pixels[37] = (off)
        pixels[36] = (off)
        pixels.show()
    
    elif number == 5:
        pixels[24] = (color)
        pixels[25] = (color)
        pixels[26] = (color)
        pixels[27] = (color)
        pixels[28] = (color)
        pixels[29] = (color)
        pixels[30] = (color)
        pixels[31] = (color)
        pixels[32] = (color)
        pixels[33] = (color)
        pixels[34] = (color)
        pixels[35] = (color)
        pixels[36] = (color)
        pixels[37] = (color)
        pixels[38] = (color)
        pixels[23] = (off)
        pixels[22] = (off)
        pixels[21] = (off)
        pixels[41] = (off)
        pixels[40] = (off)
        pixels[39] = (off)
        pixels.show()
    
    elif number == 6:
        pixels[24] = (color)
        pixels[25] = (color)
        pixels[26] = (color)
        pixels[27] = (color)
        pixels[28] = (color)
        pixels[29] = (color)
        pixels[41] = (color)
        pixels[40] = (color)
        pixels[39] = (color)
        pixels[38] = (color)
        pixels[37] = (color)
        pixels[36] = (color)
        pixels[35] = (color)
        pixels[34] = (color)
        pixels[33] = (color)
        pixels[32] = (color)
        pixels[31] = (color)
        pixels[30] = (color)
        pixels.show()

    elif number == 7:
        pixels[24] = (color)
        pixels[25] = (color)
        pixels[26] = (color)
        pixels[23] = (color)
        pixels[22] = (color)
        pixels[21] = (color)
        pixels[33] = (color)
        pixels[34] = (color)
        pixels[35] = (color)
        pixels[27] = (off)
        pixels[28] = (off)
        pixels[29] = (off)
        pixels[30] = (off)
        pixels[31] = (off)
        pixels[32] = (off)
        pixels[41] = (off)
        pixels[40] = (off)
        pixels[39] = (off)
        pixels[38] = (off)
        pixels[37] = (off)
        pixels[36] = (off)
        pixels.show()
    
    elif number == 8:
        pixels[21] = (color)
        pixels[22] = (color)
        pixels[23] = (color)
        pixels[24] = (color)
        pixels[25] = (color)
        pixels[26] = (color)
        pixels[27] = (color)
        pixels[28] = (color)
        pixels[29] = (color)
        pixels[30] = (color)
        pixels[31] = (color)
        pixels[32] = (color)
        pixels[33] = (color)
        pixels[34] = (color)
        pixels[35] = (color)
        pixels[36] = (color)
        pixels[37] = (color)
        pixels[38] = (color)
        pixels[39] = (color)
        pixels[40] = (color)
        pixels[41] = (color)
        
    elif number == 9:
        pixels[21] = (color)
        pixels[22] = (color)
        pixels[23] = (color)
        pixels[24] = (color)
        pixels[25] = (color)
        pixels[26] = (color)
        pixels[27] = (color)
        pixels[28] = (color)
        pixels[29] = (color)
        pixels[30] = (color)
        pixels[31] = (color)
        pixels[32] = (color)
        pixels[36] = (color)
        pixels[37] = (color)
        pixels[38] = (color)
        pixels[35] = (color)
        pixels[34] = (color)
        pixels[33] = (color)
        pixels[41] = (off)
        pixels[40] = (off)
        pixels[39] = (off)
        pixels.show()

# hours
def digitThree(number, color):
    if number == 0:
        pixels[44] = (color)
        pixels[45] = (color)
        pixels[46] = (color)
        pixels[47] = (color)
        pixels[48] = (color)
        pixels[49] = (color)
        pixels[50] = (color)
        pixels[51] = (color)
        pixels[52] = (color)
        pixels[56] = (color)
        pixels[57] = (color)
        pixels[58] = (color)
        pixels[59] = (color)
        pixels[60] = (color)
        pixels[61] = (color)
        pixels[62] = (color)
        pixels[63] = (color)
        pixels[64] = (color)
        pixels[53] = (off)
        pixels[54] = (off)
        pixels[55] = (off)
        pixels.show()

    elif number == 1:
        pixels[46] = (color)
        pixels[45] = (color)
        pixels[44] = (color)
        pixels[56] = (color)
        pixels[57] = (color)
        pixels[58] = (color)
        pixels[47] = (off)
        pixels[48] = (off)
        pixels[49] = (off)
        pixels[50] = (off)
        pixels[51] = (off)
        pixels[52] = (off)
        pixels[53] = (off)
        pixels[54] = (off)
        pixels[55] = (off)
        pixels[59] = (off)
        pixels[60] = (off)
        pixels[61] = (off)
        pixels[62] = (off)
        pixels[63] = (off)
        pixels[64] = (off)
        pixels.show()

    elif number == 2:
        pixels[49] = (color)
        pixels[48] = (color)
        pixels[47] = (color)
        pixels[46] = (color)
        pixels[45] = (color)
        pixels[44] = (color)
        pixels[53] = (color)
        pixels[54] = (color)
        pixels[55] = (color)
        pixels[64] = (color)
        pixels[63] = (color)
        pixels[62] = (color)
        pixels[61] = (color)
        pixels[60] = (color)
        pixels[59] = (color)
        pixels[56] = (off)
        pixels[57] = (off)
        pixels[58] = (off)
        pixels[50] = (off)
        pixels[51] = (off)
        pixels[52] = (off)
        pixels.show()

    elif number == 3:
        pixels[49] = (color)
        pixels[48] = (color)
        pixels[47] = (color)
        pixels[46] = (color)
        pixels[45] = (color)
        pixels[44] = (color)
        pixels[53] = (color)
        pixels[54] = (color)
        pixels[55] = (color)
        pixels[56] = (color)
        pixels[57] = (color)
        pixels[58] = (color)
        pixels[59] = (color)
        pixels[60] = (color)
        pixels[61] = (color)
        pixels[62] = (off)
        pixels[63] = (off)
        pixels[64] = (off)
        pixels[50] = (off)
        pixels[51] = (off)
        pixels[52] = (off)
        pixels.show()

    elif number == 4:
        pixels[50] = (color)
        pixels[51] = (color)
        pixels[52] = (color)
        pixels[53] = (color)
        pixels[54] = (color)
        pixels[55] = (color)
        pixels[56] = (color)
        pixels[57] = (color)
        pixels[58] = (color)
        pixels[46] = (color)
        pixels[45] = (color)
        pixels[44] = (color)
        pixels[49] = (off)
        pixels[48] = (off)
        pixels[47] = (off)
        pixels[64] = (off)
        pixels[63] = (off)
        pixels[62] = (off)
        pixels[61] = (off)
        pixels[60] = (off)
        pixels[59] = (off)
        pixels.show()
    
    elif number == 5:
        pixels[47] = (color)
        pixels[48] = (color)
        pixels[49] = (color)
        pixels[50] = (color)
        pixels[51] = (color)
        pixels[52] = (color)
        pixels[53] = (color)
        pixels[54] = (color)
        pixels[55] = (color)
        pixels[56] = (color)
        pixels[57] = (color)
        pixels[58] = (color)
        pixels[59] = (color)
        pixels[60] = (color)
        pixels[61] = (color)
        pixels[62] = (off)
        pixels[63] = (off)
        pixels[64] = (off)
        pixels[46] = (off)
        pixels[45] = (off)
        pixels[44] = (off)
        pixels.show()

    elif number == 6:
        pixels[47] = (color)
        pixels[48] = (color)
        pixels[49] = (color)
        pixels[50] = (color)
        pixels[51] = (color)
        pixels[52] = (color)
        pixels[53] = (color)
        pixels[54] = (color)
        pixels[55] = (color)
        pixels[56] = (color)
        pixels[57] = (color)
        pixels[58] = (color)
        pixels[59] = (color)
        pixels[60] = (color)
        pixels[61] = (color)
        pixels[62] = (color)
        pixels[63] = (color)
        pixels[64] = (color)
        pixels[44] = (off)
        pixels[45] = (off)
        pixels[46] = (off)
        pixels.show()

    elif number == 7:
        pixels[44] = (color)
        pixels[45] = (color)
        pixels[46] = (color)
        pixels[47] = (color)
        pixels[48] = (color)
        pixels[49] = (color)
        pixels[59] = (color)
        pixels[57] = (color)
        pixels[58] = (color)
        pixels[50] = (off)
        pixels[51] = (off)
        pixels[52] = (off)
        pixels[53] = (off)
        pixels[54] = (off)
        pixels[55] = (off)
        pixels[59] = (off)
        pixels[60] = (off)
        pixels[61] = (off)
        pixels[62] = (off)
        pixels[63] = (off)
        pixels[64] = (off)
        pixels.show()

    elif number == 8:
        pixels[44] = (color)
        pixels[45] = (color)
        pixels[46] = (color)
        pixels[47] = (color)
        pixels[48] = (color)
        pixels[49] = (color)
        pixels[50] = (color)
        pixels[51] = (color)
        pixels[52] = (color)
        pixels[53] = (color)
        pixels[54] = (color)
        pixels[55] = (color)
        pixels[56] = (color)
        pixels[57] = (color)
        pixels[58] = (color)
        pixels[59] = (color)
        pixels[60] = (color)
        pixels[61] = (color)
        pixels[62] = (color)
        pixels[63] = (color)
        pixels[64] = (color)
        pixels.show()
        
    elif number == 9:
        pixels[44] = (color)
        pixels[45] = (color)
        pixels[46] = (color)
        pixels[47] = (color)
        pixels[48] = (color)
        pixels[49] = (color)
        pixels[50] = (color)
        pixels[51] = (color)
        pixels[52] = (color)
        pixels[53] = (color)
        pixels[54] = (color)
        pixels[55] = (color)
        pixels[56] = (color)
        pixels[57] = (color)
        pixels[58] = (color)
        pixels[59] = (color)
        pixels[60] = (color)
        pixels[61] = (color)
        pixels[62] = (off)
        pixels[63] = (off)
        pixels[64] = (off)
        pixels.show()

# hours again
def digitFour(number, color):
    if number == 0:
        pixels[70] = (color)
        pixels[69] = (color)
        pixels[68] = (color)
        pixels[67] = (color)
        pixels[66] = (color)
        pixels[65] = (color)
        pixels[71] = (color)
        pixels[72] = (color)
        pixels[73] = (color)
        pixels[80] = (color)
        pixels[81] = (color)
        pixels[82] = (color)
        pixels[83] = (color)
        pixels[84] = (color)
        pixels[85] = (color)
        pixels[77] = (color)
        pixels[78] = (color)
        pixels[79] = (color)
        pixels[74] = (off)
        pixels[75] = (off)
        pixels[76] = (off)
        pixels.show()

    elif number == 1:
        pixels[65] = (color)
        pixels[66] = (color)
        pixels[67] = (color)
        pixels[77] = (color)
        pixels[78] = (color)
        pixels[79] = (color)
        pixels[74] = (off)
        pixels[75] = (off)
        pixels[76] = (off)
        pixels[80] = (off)
        pixels[81] = (off)
        pixels[82] = (off)
        pixels[83] = (off)
        pixels[84] = (off)
        pixels[85] = (off)
        pixels[73] = (off)
        pixels[72] = (off)
        pixels[71] = (off)
        pixels[70] = (off)
        pixels[68] = (off)
        pixels[69] = (off)
        pixels.show()

    elif number == 2:
        pixels[70] = (color)
        pixels[69] = (color)
        pixels[68] = (color)
        pixels[67] = (color)
        pixels[66] = (color)
        pixels[65] = (color)
        pixels[76] = (color)
        pixels[75] = (color)
        pixels[74] = (color)
        pixels[85] = (color)
        pixels[84] = (color)
        pixels[83] = (color)
        pixels[82] = (color)
        pixels[81] = (color)
        pixels[80] = (color)
        pixels[77] = (off)
        pixels[78] = (off)
        pixels[79] = (off)
        pixels[71] = (off)
        pixels[72] = (off)
        pixels[73] = (off)
        pixels.show()

    elif number == 3:
        pixels[70] = (color)
        pixels[69] = (color)
        pixels[68] = (color)
        pixels[67] = (color)
        pixels[66] = (color)
        pixels[65] = (color)
        pixels[74] = (color)
        pixels[75] = (color)
        pixels[76] = (color)
        pixels[77] = (color)
        pixels[78] = (color)
        pixels[79] = (color)
        pixels[80] = (color)
        pixels[81] = (color)
        pixels[82] = (color)
        pixels[85] = (off)
        pixels[84] = (off)
        pixels[83] = (off)
        pixels[71] = (off)
        pixels[72] = (off)
        pixels[73] = (off)
        pixels.show()

    elif number == 4:
        pixels[71] = (color)
        pixels[72] = (color)
        pixels[73] = (color)
        pixels[74] = (color)
        pixels[75] = (color)
        pixels[76] = (color)
        pixels[77] = (color)
        pixels[78] = (color)
        pixels[79] = (color)
        pixels[65] = (color)
        pixels[66] = (color)
        pixels[67] = (color)
        pixels[68] = (off)
        pixels[69] = (off)
        pixels[70] = (off)
        pixels[85] = (off)
        pixels[84] = (off)
        pixels[83] = (off)
        pixels[82] = (off)
        pixels[81] = (off)
        pixels[80] = (off)
        pixels.show()
    
    elif number == 5:
        pixels[68] = (color)
        pixels[69] = (color)
        pixels[70] = (color)
        pixels[71] = (color)
        pixels[72] = (color)
        pixels[73] = (color)
        pixels[74] = (color)
        pixels[75] = (color)
        pixels[76] = (color)
        pixels[77] = (color)
        pixels[78] = (color)
        pixels[79] = (color)
        pixels[80] = (color)
        pixels[81] = (color)
        pixels[82] = (color)
        pixels[85] = (off)
        pixels[84] = (off)
        pixels[83] = (off)
        pixels[67] = (off)
        pixels[66] = (off)
        pixels[65] = (off)
        pixels.show()

    elif number == 6:
        pixels[68] = (color)
        pixels[69] = (color)
        pixels[70] = (color)
        pixels[71] = (color)
        pixels[72] = (color)
        pixels[73] = (color)
        pixels[74] = (color)
        pixels[75] = (color)
        pixels[76] = (color)
        pixels[77] = (color)
        pixels[78] = (color)
        pixels[79] = (color)
        pixels[80] = (color)
        pixels[81] = (color)
        pixels[82] = (color)
        pixels[83] = (color)
        pixels[84] = (color)
        pixels[85] = (color)
        pixels[65] = (off)
        pixels[66] = (off)
        pixels[67] = (off)
        pixels.show()

    elif number == 7:
        pixels[65] = (color)
        pixels[66] = (color)
        pixels[67] = (color)
        pixels[68] = (color)
        pixels[69] = (color)
        pixels[70] = (color)
        pixels[77] = (color)
        pixels[78] = (color)
        pixels[79] = (color)
        pixels[71] = (off)
        pixels[72] = (off)
        pixels[73] = (off)
        pixels[74] = (off)
        pixels[75] = (off)
        pixels[76] = (off)
        pixels[80] = (off)
        pixels[81] = (off)
        pixels[82] = (off)
        pixels[83] = (off)
        pixels[84] = (off)
        pixels[85] = (off)
        pixels.show()

    elif number == 8:
        pixels[65] = (color)
        pixels[66] = (color)
        pixels[67] = (color)
        pixels[68] = (color)
        pixels[69] = (color)
        pixels[70] = (color)
        pixels[71] = (color)
        pixels[72] = (color)
        pixels[73] = (color)
        pixels[74] = (color)
        pixels[75] = (color)
        pixels[76] = (color)
        pixels[77] = (color)
        pixels[78] = (color)
        pixels[79] = (color)
        pixels[80] = (color)
        pixels[81] = (color)
        pixels[82] = (color)
        pixels[83] = (color)
        pixels[84] = (color)
        pixels[85] = (color)
        pixels.show()
    
    elif number == 9:
        pixels[65] = (color)
        pixels[66] = (color)
        pixels[67] = (color)
        pixels[68] = (color)
        pixels[69] = (color)
        pixels[70] = (color)
        pixels[71] = (color)
        pixels[72] = (color)
        pixels[73] = (color)
        pixels[74] = (color)
        pixels[75] = (color)
        pixels[76] = (color)
        pixels[77] = (color)
        pixels[78] = (color)
        pixels[79] = (color)
        pixels[80] = (color)
        pixels[81] = (color)
        pixels[82] = (color)
        pixels[83] = (off)
        pixels[84] = (off)
        pixels[85] = (off)
        pixels.show()

# Example
# digitOne(2, (255, 0 , 0))

digit1 = 0
digit2 = 0
digit3 = 0
digit4 = 0

digitOne(digit1, (brightness))
digitTwo(digit2, (brightness))
digitThree(digit3, (brightness))
digitFour(digit4, (brightness))
pixels[42] = (brightness)
pixels[43] = (brightness)
pixels.show()

while True:

    currentTime = datetime.datetime.now()

    minutes = (currentTime.minute)
    hours = (currentTime.hour)

    # Minutes
    if minutes <= 9:
        digit1 = minutes
        digit2 = 0
    elif minutes > 9:
        string = [int(i) for i in str(minutes)]
        digit1 = (string[1])
        digit2 = (string[0])

    # Hours
    if hours <= 9:
        digit3 = hours
        digit4 = 0
    elif hours > 9:
        hours2 = hours - 12
        if hours2 == 0:
            digit3 = 2
            digit4 = 1
        elif hours2 <= 9:
            digit3 = hours2
            digit4 = 0
        elif hours2 > 9:
            string2 = [int(i) for i in str(hours2)]
            digit3 = (string2[1])
            digit4 = (string2[0])

    pixels[42] = (brightness)
    pixels[43] = (brightness)
    digitOne(digit1, (brightness))
    digitTwo(digit2, (brightness))
    digitThree(digit3, (brightness))
    digitFour(digit4, (brightness))