import requests
from datetime import datetime

placeuser = input("Please enter the place : ")

url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"q":placeuser,"lat":"0","lon":"0","id":"2172797","lang":"null","units":"imperial"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "Enter Your API Key here"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

def convertC(f):
  return float((f-32)*(5/9))

data = response.json()
temp = convertC(data['main']['temp'])
tempmax = convertC(data['main']['temp_max'])
tempmin = convertC(data['main']['temp_min'])

print("-----------Location------------------ ")
print( data["name"], data["sys"]["country"])

print("-------------Date:--------------------- ")
print("Sunrise: ", datetime.fromtimestamp(data["sys"]["sunrise"]))
print("Sunset: ", datetime.fromtimestamp(data["sys"]["sunset"]))

print("-------------------------Weather-------------------------")
print("Description:", data["weather"][0]["description"])

print("--------------------------Temperature------------------ ")
print("Current Temperature: " ,f"{round(temp,2)} C"  )
print("Max Temperature: " ,f"{round(tempmax,2)} C"  )
print("Min Temperature: " ,f"{round(tempmin,2)} C"  )

