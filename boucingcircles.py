import win32api as api
import win32gui as gui
import random
import time

def boucingcircles():
    sw = api.GetSystemMetrics(0)
    sh = api.GetSystemMetrics(1)
    x = 10
    y = 10
    dx = 10
    dy = 10
    size = 116
    while True:
        hdc = gui.GetDC(0)
        x += dx
        y += dy

        if x <= 0 or x + size >= sw:
            dx *= -1

        if y <= 0 or y + size >= sh:
            dy *= -1

        brush = gui.CreateSolidBrush(api.RGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        old = gui.SelectObject(hdc, brush)

        gui.Ellipse(hdc, x, y, x + size, y + size)
        
        gui.SelectObject(hdc, old)
        gui.DeleteObject(brush)
        gui.ReleaseDC(0, hdc)

        time.sleep(1/60)
time.sleep(1)
boucingcircles()