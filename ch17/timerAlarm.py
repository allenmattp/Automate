#! python3
# timerAlarm.py - sets an alert x minutes from being launched.


import datetime, time, ctypes, sys

"""
if float(sys.argv[1]):
    minToWait = float(sys.argv[1])
else:
    print("Enter 'timer minutes' where minutes is desired length of timer.")
    sys.exit()"""
minToWait = 1.

waitTime = datetime.timedelta(minutes=minToWait)
startTime = datetime.datetime.now()
endTime = startTime + waitTime

print(waitTime, startTime, endTime)

print(f"Waiting for {waitTime} minute(s) ...")
while datetime.datetime.now() < endTime:
    time.sleep(1)
    print(endTime - datetime.datetime.now())     # comment out or adjust time.sleep

ctypes.windll.user32.MessageBoxW(0, "Time has expired!", "Alert", 1)