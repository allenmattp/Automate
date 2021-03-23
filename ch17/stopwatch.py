#! python3
# stopwatch.py - A simple stopwatch program.

import time

# user instructions
print("Press ENTER to begin.\n"
      "While running, press ENTER to 'click' the stopwatch\n"
      "Press Ctrl-C to quit.")

input() # press enter to begin
print("Clock started.")
startTime = time.time()
lastTime = startTime
lapNum = 1


# TODO: Start tracking the laps times
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print(f"Lap {lapNum}: {totalTime} ({lapTime)}", end="")
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to suppress error message
    print("\nDone")