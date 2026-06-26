import win32gui as gui
import win32api as api
import win32ui as ui
import win32con as con
import random
import time

def randomtexts():
    sw = api.GetSystemMetrics(0)
    sh = api.GetSystemMetrics(1)
    font = ui.CreateFont({"name": "Default", "height": 50, "weight": 400, "underline": True, "italic": True})
    while True:
        hdc = gui.GetDC(0)
        dc = ui.CreateDCFromHandle(hdc)
        dc.SelectObject(font)
        x = random.randint(0, sw)
        y = random.randint(0, sh)
        dc.SetBkColor(api.RGB(0, 0, 0))
        dc.SetTextColor(
            api.RGB(
                random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            )
        )
        gui.ExtTextOut(hdc, x, y, 0, None, "ExtTextOut", None)

        gui.ReleaseDC(0, hdc)
        time.sleep(1/10)

randomtexts()