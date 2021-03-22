#! python3
# getOpenWeather.py - Prints weather for an entered location

import openWeatherAPI

# put your API token here
APPID = openWeatherAPI.getToken()

import json, requests, sys, pprint

# Compute location from command line argument
if len(sys.argv) < 2:
    print("Usage: getOpenWeather.py city_name, 2-letter_country_code")
    sys.exit()
location = " ".join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API
url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=imperial&APPID={APPID}"
response = requests.get(url)
response.raise_for_status()

#pprint.pprint(response.text)

# Load JSON data into a python variable
weatherData = json.loads(response.text)

main = weatherData["main"]
print(f"Current weather in {location}:")
print(weatherData["weather"][0]["description"])
print(f'Temp: {main["temp"]}, feels like {main["feels_like"]}')
print(f'Max: {main["temp_max"]}, Min: {main["temp_min"]}')