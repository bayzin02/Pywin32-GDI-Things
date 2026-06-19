import win32gui as gui
import win32con as con
import win32api as api
import random
import time

def rainbow():
    sw = api.GetSystemMetrics(0)
    sh = api.GetSystemMetrics(1)
    while True:
        hdc = gui.GetDC(0)

        brush = gui.CreateSolidBrush(api.RGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        old = gui.SelectObject(hdc, brush)

        gui.PatBlt(hdc, 0, 0, sw, sh, con.PATINVERT)
        
        gui.SelectObject(hdc, old)
        gui.DeleteObject(brush)
        gui.ReleaseDC(0, hdc)
        time.sleep(1/20)

time.sleep(1)
rainbow()