import win32gui as gui
import win32con as con
import time

def cursor():
    icon = gui.LoadIcon(0, con.IDI_ERROR)
    while True:
        hdc = gui.GetDC(0)
        x, y = gui.GetCursorPos()
        gui.DrawIconEx(hdc, (x - 32), (y - 32), icon, 32, 32, 0, 0, con.DI_NORMAL)

        gui.ReleaseDC(0, hdc)
        time.sleep(1/144)

time.sleep(1)
cursor()