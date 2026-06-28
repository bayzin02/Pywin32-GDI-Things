import win32gui as gui
import win32con as con
import win32api as api
import random, time

def xorshift():
    sw = api.GetSystemMetrics(0)
    sh = api.GetSystemMetrics(1)
    while True:
        hdc = gui.GetDC(0)
        gui.BitBlt(
            hdc,
            random.randint(-5, 5),
            random.randint(-5, 5),
            sw,
            sh,
            hdc,
            random.randint(-5, 5),
            random.randint(-5, 5),
            con.SRCINVERT,
        )
        gui.ReleaseDC(0, hdc)

time.sleep(1)
xorshift()
