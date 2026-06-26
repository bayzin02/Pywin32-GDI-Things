import win32gui as gui
import win32con as con
import win32api as api
import random
import time

def randowicons():
    sw = api.GetSystemMetrics(0)
    sh = api.GetSystemMetrics(1)
    IDI_SHIELD = 32518
    listicons = [
        con.IDI_APPLICATION,
        con.IDI_ASTERISK,
        con.IDI_ERROR,
        con.IDI_EXCLAMATION,
        con.IDI_HAND,
        con.IDI_INFORMATION,
        con.IDI_QUESTION,
        con.IDI_WARNING,
        IDI_SHIELD,
    ]
    while True:
        hdc = gui.GetDC(0)
        for icon in listicons:
            gui.DrawIcon(
                hdc,
                random.randint(0, sw - 32),
                random.randint(0, sh - 32),
                gui.LoadIcon(None, icon)
            )
        gui.ReleaseDC(0, hdc)
        time.sleep(1/144)

time.sleep(1)
randowicons()