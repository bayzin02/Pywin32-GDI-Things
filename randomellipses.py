import win32gui as gui
import win32con as con
import win32api as api
import random, time

def randomellipses():
    sw = api.GetSystemMetrics(0)
    sh = api.GetSystemMetrics(1)
    ballsize = 160
    while True:
        x = random.randint(0, sw - 32)
        y = random.randint(0, sh - 32)
        hdc = gui.GetDC(0)
        brush = gui.CreateSolidBrush(
            api.RGB(
                random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            )
        )
        old = gui.SelectObject(hdc, brush)
        gui.Ellipse(hdc, x, y, x + ballsize, y + ballsize)

        gui.SelectObject(hdc, old)
        gui.DeleteObject(old)
        gui.DeleteObject(brush)
        gui.ReleaseDC(0, hdc)
        time.sleep(1/10)
randomellipses()