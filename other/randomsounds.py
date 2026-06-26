import winsound
import random
import time

def randomsounds():
    sounds = [
        "SystemAsterisk",
        "SystemHand",
        "MailBeep",
        r"C:\Windows\Media\Windows Critical Stop.wav",
        "SystemAsterisk",
        "SystemHand",
        "MailBeep",
        r"C:\Windows\Media\Windows Critical Stop.wav",
    ]
    while True:
        winsound.PlaySound(random.choice(sounds), winsound.SND_ALIAS)

time.sleep(1)
randomsounds()