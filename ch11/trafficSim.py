mercer_5th = {"ns": "green", "ew": "red"}
pine_3rd = {"nwse": "green", "nesw": "red"}

def switchLights(stoplight):
    for k in stoplight.keys():
        if stoplight[k] == "green":
            stoplight[k] = "yellow"
        elif stoplight[k] == "yellow":
            stoplight[k] = "red"
        elif stoplight[k] == "red":
            stoplight[k] = "green"
    assert "red" in stoplight.values(), "No lights are red! " + str(stoplight)

switchLights(mercer_5th)

