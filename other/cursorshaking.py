# A small warning: this is somewhat dangerous to test on your actual machine; I don't recommend it.

import win32gui as gui
import win32api as api
import random
import time

def cursorshaking():
    while True:
        x, y = gui.GetCursorPos()

        api.SetCursorPos(( x + random.randint(-3, 3), y + random.randint(-3, 3) ))
        time.sleep(0.01) # I not recommend your put 0 here btw

time.sleep(1)
cursorshaking()