import time
import win32api as api
import win32con as con
import win32gui as gui

def train():
    sw = api.GetSystemMetrics(0)
    sh = api.GetSystemMetrics(1)
    while True:
        hdc = gui.GetDC(0)

        gui.BitBlt(hdc, -15, 0, sw, sh, hdc, 0, 0, con.SRCCOPY)
        gui.BitBlt(hdc, sw - 15, 0, sw, sh, hdc, 0, 0, con.SRCCOPY)
        gui.ReleaseDC(0, hdc)

time.sleep(1)
train()