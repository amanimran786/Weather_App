
import requests

def get_weather(city, unit):
    api_key = "493960142acebccb3ba21c30f34bd019"  # Your API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={unit}"
    response = requests.get(url)
    data = response.json()
    return data
