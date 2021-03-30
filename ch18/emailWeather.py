#! python3
# getOpenWeather.py - Emails weather report to specified address

import openWeatherAPI

# put your API token here
APPID = openWeatherAPI.getToken()

import json, requests, sys, pprint, smtplib, passwordGen

# location for weather
location = "Seattle, US"

# Download the JSON data from OpenWeatherMap.org's API
url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=imperial&APPID={APPID}"
response = requests.get(url)
response.raise_for_status()

#pprint.pprint(response.text)

# Load JSON data into a python variable
weatherData = json.loads(response.text)

main = weatherData["main"]
printLocation = f"Current weather in {location}:"
printDescription = weatherData["weather"][0]["description"]
printTemp = f'Temp: {main["temp"]}, feels like {main["feels_like"]}'
printRange = f'Max: {main["temp_max"]}, Min: {main["temp_min"]}'

emailBody = f"""
{printLocation}
{printDescription}
{printTemp}
{printRange}
"""

conn = smtplib.SMTP("smtp.gmail.com", 587)

conn.ehlo()
conn.starttls()

# grab my app password so I don't upload it to github
password = passwordGen.passGen()

conn.login("allenmattpdev@gmail.com", password)

conn.sendmail("allenmattpdev@gmail.com", "allenmattp@gmail.com",
              "Subject: Weather Report\n\n" +
              emailBody)

conn.quit()