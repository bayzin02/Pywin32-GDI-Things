import win32gui as gui
import win32api as api
import win32con as con
import random
import time

def slice():
    sw = api.GetSystemMetrics(0)
    sh = api.GetSystemMetrics(1)
    while True:
        hdc = gui.GetDC(0)

        y = random.randint(0, sh - 5)
        x = random.choice([-40, -30, 30, 40])
        gui.BitBlt(hdc, x, y, sw, 64, hdc, 0, y, con.SRCCOPY)

        gui.ReleaseDC(0, hdc)
        time.sleep(0.1)
time.sleep(1)
slice()