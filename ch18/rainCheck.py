#! python3
# rainCheck.py - Emails current weather along with 7 day forecast.
# Includes callouts for any inclement weather expected over the next 48 hours.

import openWeatherAPI

# put your API token here
APPID = openWeatherAPI.getToken()

import json, requests, pprint, smtplib, passwordGen
from datetime import datetime

# location for weather
location = "Seattle, US"    # future project: pull location from lat/lon or vice versa
lat = 47.6062
lon = -122.3321

# Download the JSON data from OpenWeatherMap.org's API
url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely&units=imperial&APPID={APPID}"
response = requests.get(url)
response.raise_for_status()

#pprint.pprint(response.text)

# Load JSON data into a python variable
weatherData = json.loads(response.text)

current = weatherData["current"]
currentTemp = f'Current temp is {current["temp"]}; feels like {current["feels_like"]}. '
currentDesc = f'Currently {current["weather"][0]["description"]}.\n\n'

# check for any inclement weather (anything other than clear/cloudy)
alerts = []
for h in weatherData["hourly"]:
    w = str(h["weather"][0]["id"])
    if w[0] == "2" or w[0] == "3" or w[0] == "5" or w[0] == "6" or w[0] == "7":
        desc = h["weather"][0]["description"]
        dt = int(h["dt"])
        alerts.append(f"Watch out for a {desc} {datetime.utcfromtimestamp(dt).strftime('%A about %I:%M %p')}\n\n")
    #print(w)

# collect daily forecast
daily = []
for d in weatherData["daily"]:
    dt = datetime.utcfromtimestamp(int(d["dt"])).strftime('%A, %b %d')
    temp = f'{dt}: Daytime temp of {d["temp"]["day"]}, high of {d["temp"]["max"]} and low of {d["temp"]["min"]}. '
    w = f'Expect {str(d["weather"][0]["main"])}.\n\n'
    daily.append(temp + w)

# format the weather report
alertString = ""
dailyString = ""
emailBody = currentTemp + currentDesc + \
            "In the next 48 hours...\n\n" + alertString.join(alerts) +\
            "Over the next 7 days...\n\n" + dailyString.join(daily)


# send the weather report via SMTP
conn = smtplib.SMTP("smtp.gmail.com", 587)
conn.ehlo()
conn.starttls()

# grab my app password so I don't upload it to github
password = passwordGen.passGen()
conn.login("allenmattpdev@gmail.com", password)
conn.sendmail("allenmattpdev@gmail.com", "allenmattp@gmail.com",
              f"Subject: {location} Weather Forecast\n\n" +
              emailBody)

conn.quit()