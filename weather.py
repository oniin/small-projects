import requests
from pprint import pprint

API_Key = '4f0d4c499d25eae84d7a051cd23e508a'

city = input("Enter the city:  ").lower()

# base_url = "https://openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city
base_url = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()



pprint(weather_data)
