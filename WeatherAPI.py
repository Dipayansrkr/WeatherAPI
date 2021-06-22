import requests
# import os
from datetime import datetime

api_key = 'a053626c396619029760d99ea485e928'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("-------------------------------------------------------------")
print("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print("-------------------------------------------------------------")

print("Current temperature is: {:.2f} deg C".format(temp_city))
print("Current weather desc  :", weather_desc)
print("Current Humidity      :", hmdt, '%')
print("Current wind speed    :", wind_spd, 'kmph')

weather = open('record.txt', 'w')
weather.write("-------------------------------------------------------------\n")
weather.write("Weather Stats for - {}  || {} \n".format(location.upper(), date_time))
weather.write("------------------------------------------------------------- \n")

weather.write("Current temperature is: {:.2f} deg C".format(temp_city))
weather.write("Current Weather Description  :" + weather_desc+'\n')
weather.write("Current Humidity      :" +str(hmdt) + ' % \n')
weather.write("Current wind speed    :" + str(wind_spd) + ' kph \n')
weather.close()
