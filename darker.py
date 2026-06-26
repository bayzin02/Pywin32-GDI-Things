import win32api as api
import win32gui as gui
import win32con as con
import random
import time

def darker():
    sw = api.GetSystemMetrics(0)
    sh = api.GetSystemMetrics(1)
    while True:
        hdc = gui.GetDC(0)
        gui.BitBlt(hdc, random.randint(-1, 1), random.randint(-1, 1), sw, sh, hdc, 0, 0, con.SRCAND)
        gui.ReleaseDC(0, hdc)
        time.sleep(1/60)
time.sleep(1)
darker()