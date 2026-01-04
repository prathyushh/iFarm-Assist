import httpx
import os
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

async def get_current_weather(location: str):
    """
    Fetches real-time weather from OpenWeatherMap.
    Returns a formatted string for the AI context.
    """
    if not OPENWEATHER_API_KEY:
        print("WARNING: OPENWEATHER_API_KEY not found. Using Mock Data.")
        return "Current Weather (Mock): 30°C, Sunny, Humidity: 75%."

    try:
        async with httpx.AsyncClient() as client:
            params = {
                "q": location,
                "appid": OPENWEATHER_API_KEY,
                "units": "metric" # Celcius
            }
            response = await client.get(BASE_URL, params=params, timeout=5.0)
            
            if response.status_code == 200:
                data = response.json()
                temp = data["main"]["temp"]
                desc = data["weather"][0]["description"]
                humidity = data["main"]["humidity"]
                
                return f"Current Weather in {location}: {temp}°C, {desc.title()}, Humidity: {humidity}%."
            else:
                print(f"Weather API Error: {response.text}")
                return f"Current Weather: Unavailable (API Error)."
                
    except Exception as e:
        print(f"Weather Fetch Failed: {e}")
        return "Current Weather: Unavailable."
