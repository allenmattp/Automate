import traceback, time


t = time.localtime()
current_time = time.strftime("%m-%d-%Y %I:%M:%S%p")

try:
    raise Exception("The program takes exception to that.")
except:
    with open("errorReport.txt", "a") as f:
        f.write(f"\n\nCurrent time: {current_time}\n")
        f.write(traceback.format_exc())
        print("The traceback information was noted in the errorReport.txt.")
    f.close()