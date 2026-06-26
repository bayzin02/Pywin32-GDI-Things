import win32api as api
import win32con as con
import win32gui as gui
import time

def tunnel():
    sw = api.GetSystemMetrics(0)
    sh = api.GetSystemMetrics(1)
    while True:
        hdc = gui.GetDC(0)

        gui.StretchBlt(hdc, 75, 75, sw - 150, sh - 150, hdc, 0, 0, sw, sh, con.SRCCOPY)

        gui.ReleaseDC(0, hdc)
        time.sleep(0.1)
time.sleep(1)
tunnel()