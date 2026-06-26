import win32gui as gui
import win32api as api
import time

def setpixel():
    sw = api.GetSystemMetrics(0)
    sh = api.GetSystemMetrics(1)
    while True:
        hdc = gui.GetDC(0)

        for y in range(sh):
            for x in range(sw):
                draw = (x * 6) & 255

                gui.SetPixel(hdc, x, y, api.RGB(draw, draw, draw))

        gui.ReleaseDC(0, hdc)

time.sleep(1)
setpixel()