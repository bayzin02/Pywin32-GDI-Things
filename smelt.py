import win32gui as gui
import win32con as con
import win32api as api
import random
import time

def smelt():
    sw = api.GetSystemMetrics(0)
    sh = api.GetSystemMetrics(1)
    while True:
        hdc = gui.GetDC(0)
        wx = random.randint(0, sw - 32)
        gui.BitBlt(hdc, wx, 10, random.randint(50, 100), sh, hdc, wx, 0, con.SRCCOPY)
        gui.ReleaseDC(0, hdc)

time.sleep(1)
smelt()