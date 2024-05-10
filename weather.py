import requests
api_key = '30d4741c779ba94c470ca1f63045390a'
user_input = input("Enter city: ")
weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
if weather_data.json ( ) ['cod'] == '404':
           print("No City Found")
else:
    weather = weather_data.json ( ) ['weather'][0]['main']
    temp = round(weather_data.json( ) ['main'] ['temp'])
    humidity = weather_data.json()['main']['humidity']
    windspeed=weather_data.json()['wind']['speed']
    print (f"The weather in {user_input} is: {weather}")
    print (f"The temperatupre in {user_input} is: {temp}°F")
    print (f"The humidity in {user_input} is: {humidity}°F")
    print (f"The windspeed in {user_input} is: {windspeed}°F")