import requests

API_KEY = "1e9e02fd52b553675dca10b361669948"  
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

city = input("Enter city name: ")

url = BASE_URL + "appid=" + API_KEY + "&q=" + city + "&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] != "404":
    main = data["main"]
    temperature = main["temp"]
    humidity = main["humidity"]
    pressure = main["pressure"]
    weather = data["weather"][0]["description"]

    report = (f"🌍 City: {city}\n"
              f"🌡️ Temperature: {temperature}°C\n"
              f"💧 Humidity: {humidity}%\n"
              f"⏲️ Pressure: {pressure} hPa\n"
              f"☁️ Weather: {weather}")
    
    print("\nWeather Report:\n", report)

else:
    print(" City not found!")
