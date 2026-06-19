import time

red = 0  # Hue Function Inspired in void_/GetMBR Hue
green = 0
blue = 0
lockblue = False
phase = 0

def hue(color=255):
    global red, green, blue, phase, lockblue
    if phase == 0:
        red += 1
        if red == color:
            phase = 1
    elif phase == 1:
        blue = 0
        green += 1
        if green == color:
            phase = 2
    elif phase == 2:
        red = 0
        blue += 1
        if blue == color:
            phase = 3
    elif phase == 3:
        red = 0
        green = 0
        blue = 0
        phase = 0
        lockblue = True
        if lockblue == True:
            blue = 255
        else:
            pass
        return red, green, blue, phase

while True:
    hue()
    print(f" Red: {red} | Green: {green} | Blue: {blue}", end="\r")
    time.sleep(0.02)