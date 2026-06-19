import win32gui as gui
import win32con as con
import win32api as api
import time

def invert():
    sw = api.GetSystemMetrics(0)
    sh = api.GetSystemMetrics(1)
    while True:
        hdc = gui.GetDC(0)

        gui.PatBlt(hdc, 0, 0, sw, sh, con.PATINVERT)

        gui.ReleaseDC(0, hdc)
        time.sleep(2)

time.sleep(1)
invert()