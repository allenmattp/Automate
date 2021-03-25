import threading, time


print("Start of program.")

def takeANap():
    time.sleep(5)
    print("Wake up!")

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print("End of program.")

thread2Obj = threading.Thread(target=print, args=["Cat", "Dogs", "Frogs"],
                              kwargs={"sep": " & "})
thread2Obj.start()