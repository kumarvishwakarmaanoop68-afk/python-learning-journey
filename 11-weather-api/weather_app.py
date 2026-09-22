"""Day 11 - Weather API App"""

import json
import requests

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"
FILE_NAME = "latest_weather.json"


class WeatherApi:
    def find_city(self, city):
        params = {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }

        try:
            response = requests.get(GEOCODING_URL, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            results = data.get("results", [])

            if not results:
                return None

            return results[0]
        except requests.Timeout:
            print("Location request timed out.")
        except requests.RequestException as error:
            print("Location request failed:", error)
        except ValueError:
            print("Invalid location API response.")

        return None

    def get_weather(self, latitude, longitude):
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
            "timezone": "auto"
        }

        try:
            response = requests.get(WEATHER_URL, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.Timeout:
            print("Weather request timed out.")
        except requests.RequestException as error:
            print("Weather request failed:", error)
        except ValueError:
            print("Invalid weather API response.")

        return None


class WeatherApp:
    def __init__(self):
        self.api = WeatherApi()

    @staticmethod
    def weather_description(code):
        descriptions = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Fog",
            48: "Depositing rime fog",
            51: "Light drizzle",
            53: "Moderate drizzle",
            55: "Dense drizzle",
            61: "Slight rain",
            63: "Moderate rain",
            65: "Heavy rain",
            71: "Slight snow",
            73: "Moderate snow",
            75: "Heavy snow",
            80: "Slight rain showers",
            81: "Moderate rain showers",
            82: "Violent rain showers",
            95: "Thunderstorm"
        }
        return descriptions.get(code, "Unknown condition")

    def run(self):
        city = input("Enter city name: ").strip()

        if not city:
            print("City name cannot be empty.")
            return

        location = self.api.find_city(city)

        if not location:
            print("City not found.")
            return

        weather = self.api.get_weather(
            location["latitude"],
            location["longitude"]
        )

        if not weather:
            return

        current = weather.get("current", {})
        units = weather.get("current_units", {})

        result = {
            "city": location.get("name"),
            "country": location.get("country"),
            "temperature": current.get("temperature_2m"),
            "temperature_unit": units.get("temperature_2m", "°C"),
            "humidity": current.get("relative_humidity_2m"),
            "humidity_unit": units.get("relative_humidity_2m", "%"),
            "wind_speed": current.get("wind_speed_10m"),
            "wind_unit": units.get("wind_speed_10m", "km/h"),
            "condition": self.weather_description(current.get("weather_code"))
        }

        print("\n===== Current Weather =====")
        print(f"Location    : {result['city']}, {result['country']}")
        print(f"Temperature : {result['temperature']} {result['temperature_unit']}")
        print(f"Condition   : {result['condition']}")
        print(f"Humidity    : {result['humidity']}{result['humidity_unit']}")
        print(f"Wind Speed  : {result['wind_speed']} {result['wind_unit']}")

        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(result, file, indent=4)

        print("\nLatest weather saved to latest_weather.json.")


if __name__ == "__main__":
    WeatherApp().run()
