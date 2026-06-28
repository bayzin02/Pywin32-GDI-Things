import win32gui as gui
import win32api as api
import time

def setpixel():
    sw = api.GetSystemMetrics(0)
    sh = api.GetSystemMetrics(1)
    while True:
        hdc = gui.GetDC(0)

        for y in range(sh):
            gui.PatBlt(hdc, 0, y, 0, sh, )

        gui.ReleaseDC(0, hdc)

time.sleep(1)
setpixel()