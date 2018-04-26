#! python3
# quickWeather.py - Prints the current weather for a location from the command line.

import json, requests, sys

# Download the JSON data from OpenWeatherMap.org's API
url ='api.openweathermap.org/data/2.5/forecast/daily?q=London&mode=xml&units=metric&cnt=7'
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# Print weather descriptions.
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
