import win32gui as gui
import win32api as api
import win32con as con
import time

def verticalinvert():
    sw = api.GetSystemMetrics(0)
    sh = api.GetSystemMetrics(1)
    while True:
        hdc = gui.GetDC(0)
        for y in range(0, sh, 12):
            gui.PatBlt(hdc, 0, y, sw, 8, con.DSTINVERT)
        gui.ReleaseDC(0, hdc)

time.sleep(1)
verticalinvert()