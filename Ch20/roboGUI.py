import pyautogui, time

wh = pyautogui.size()   # get resolution
print(wh)
print(wh[0])
print(wh.width)

# return position of cursor at time function is called
for i in range(5):
    time.sleep(.25)
    print(pyautogui.position())

# move mouse on absolute coordinates
for i in range(2):
    pyautogui.moveTo(100, 100, duration=.25)
    print(pyautogui.position())
    pyautogui.moveTo(200, 100, duration=.25)
    print(pyautogui.position())
    pyautogui.moveTo(200, 200, duration=.25)
    print(pyautogui.position())
    pyautogui.moveTo(100, 200, duration=.25)
    print(pyautogui.position())

# move mouse on relative coordinates
for i in range(2):
    pyautogui.move(100, 0, duration=.25)
    print(pyautogui.position())
    pyautogui.move(0, 100, duration=.25)
    print(pyautogui.position())
    pyautogui.move(-100, 0, duration=.25)
    print(pyautogui.position())
    pyautogui.move(0, -100, duration=.25)
    print(pyautogui.position())

pyautogui.click(10, 5)      # Move mouse to (10, 5) and click