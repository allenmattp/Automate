import pyautogui, time

wh = pyautogui.size()   # get resolution
print(wh)
print(wh[0])
print(wh.width)

# return position of cursor at time function is called
for i in range(5):
    print(pyautogui.position())
    time.sleep(.25)

# move mouse on absolute coordinates
for i in range(5):
    pyautogui.moveTo(100, 100, duration=.25)
    pyautogui.moveTo(200, 100, duration=.25)
    pyautogui.moveTo(200, 200, duration=.25)
    pyautogui.moveTo(100, 200, duration=.25)

# move mouse on relative coordinates
for i in range(5):
    pyautogui.move(100, 0, duration=.25)
    pyautogui.move(0, 100, duration=.25)
    pyautogui.move(-100, 0, duration=.25)
    pyautogui.move(0, -100, duration=.25)