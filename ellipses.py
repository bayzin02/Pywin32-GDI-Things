import win32gui as gui
import win32con as con
import win32api as api
import random, time

def ellipses():
    sw = api.GetSystemMetrics(0)
    sh = api.GetSystemMetrics(1)
    while True:
        hdc = gui.GetDC(0)
        brush = gui.CreateSolidBrush(
            api.RGB(
                random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            )
        )
        old = gui.SelectObject(hdc, brush)
        gui.Ellipse(
            hdc,
            random.randint(0, sw),
            random.randint(0, sh),
            random.randint(0, sw),
            random.randint(0, sh),
        )
        gui.SelectObject(hdc, old)
        gui.DeleteObject(old)
        gui.DeleteObject(brush)
        gui.ReleaseDC(0, hdc)
        time.sleep(1/30)
ellipses()