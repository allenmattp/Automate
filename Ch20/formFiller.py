#! python3
# formFiller.py - Automatically fill in form located at https://autbor.com/form

import pyautogui, time, webbrowser

# Open form
webbrowser.open('https://autbor.com/form')
print('Ensure that the browser window is active and the form is loaded!')

pyautogui.PAUSE = 0.5

# data to enter into form
# could be pulled from another source if desired
# source must begin with "w", "a", "d" or "m"
formData = [
    {'name': "Niles",
    'fear': "Starvation",
    'source': "Discount Crystal Ball",
    'robocop': 3,
    'comments': "Thanks for the great book!"},
    {'name': "Carol",
    'fear': "Puppets",
    'source': "amulet",
    'robocop': 1,
    'comments': "Please take the puppets out of the break room"},
    {'name': "Alex Murphy",
    'fear': "ED-209",
    'source': "Money",
    'robocop': 5,
    'comments': "Protect the innocent. Serve the public trust. Uphold the law."},
    {'name': "Alice",
    'fear': "Animals",
    'source': "wand",
    'robocop': 4,
    'comments': "Don't trust food labels."}
]
for data in formData:
    # Give the user a chance to kill script
    print(">>> YOU HAVE 5 SECONDS TO CANCEL (CTRL-C) <<<")
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    print(f"Entering {data['name']}")
    pyautogui.write(["\t", "\t"])

    # Fill out the text fields
    pyautogui.write(data["name"] + "\t")
    pyautogui.write(data["fear"] + "\t")

    # Type first letter of Wizard Source to select it in dropdown
    pyautogui.write(data["source"][0])
    pyautogui.write("\t")

    # Press space to select a radio button
    pyautogui.write(" ")
    # Move selection to the right appropriate number of times
    # (or don't move if user entered 1)
    if data["robocop"] > 1:
        for n in range(1, data["robocop"]):
            pyautogui.write(["right"], 0.25)
    pyautogui.write(["\t", "\t"])

    # Fill out additional comments
    pyautogui.write(data["comments"] + "\t")

    # Click Submit
    pyautogui.press("enter")

    # Allow time for form to submit
    print("Form submitted.")
    time.sleep(2)

    # Click the Submit another response link
    pyautogui.write("\t")
    pyautogui.press("enter")