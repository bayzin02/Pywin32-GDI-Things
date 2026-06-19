import win32gui as gui
import win32con as con
import win32api as api
import random
import time

def blocks():
    sw = api.GetSystemMetrics(0)
    sh = api.GetSystemMetrics(1)
    while True:
        hdc = gui.GetDC(0)

        gui.BitBlt(
            hdc,
            random.randint(0, sh - random.randint(50, 100)),
            random.randint(0, sw - random.randint(50, 100)),
            random.randint(0, sh - random.randint(50, 100)),
            random.randint(0, sw - random.randint(50, 100)),
            hdc,
            random.randint(10, sw - 100),
            random.randint(10, sh - 100),
            con.SRCCOPY,
        )
        gui.ReleaseDC(0, hdc)
        time.sleep(0.2)

time.sleep(1)
blocks()