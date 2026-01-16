import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
def get_weather(city: str) -> dict:
    """
    Fetch current weather for a given city.
    Returns structured weather data.
    """

    if not OPENWEATHER_API_KEY:
        raise ValueError("OpenWeather API key not found")

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"   # Celsius
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return {
            "error": f"Could not fetch weather for {city}"
        }

    data = response.json()

    weather_info = {
        "city": data["name"],
        "temperature_c": data["main"]["temp"],
        "condition": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed_kmph": data["wind"]["speed"] * 18/5
    }

    return weather_info


# 🔍 Manual test
if __name__ == "__main__":
    city = "New Delhi"
    weather = get_weather(city)
    print(weather)
