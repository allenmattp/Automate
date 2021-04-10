#! python3
# noSleep.py - periodically move mouse to avoid inactivity

import pyautogui, random

# wait between each move
pyautogui.PAUSE = 30

while True:
    pyautogui.move(random.randint(-100, 100), random.randint(-100, 100), random.random())