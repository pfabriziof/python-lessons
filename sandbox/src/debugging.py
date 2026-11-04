from pydantic import BaseModel
from typing import TypedDict

class WeatherDict(TypedDict):
    id: int
    temperature: float
    weather_type: str  # Optional if some cities omit it

class ApiResponse(BaseModel):
    id: int = 0
    temperature: float = 0.
    weather_type: str = ""

# we don’t see the contents of this method, pretend this is what an actual HTTP API call returns
def fake_weather_api_request(city: str) -> WeatherDict:
    cities = {"New York": {"id": 42, "temperature": 25.6, "weather_type": "sunny"},
              "Marrakech": {"id": 12, "temperature": 30}}
    if city not in cities:
        raise ValueError(f"City '{city}' not found")
    return cities[city]

if __name__ == "__main__":
    # breakpoint()
    weather_resp = fake_weather_api_request("New York")
    ny_weather = ApiResponse(**weather_resp)
    print(f"Weather in New York (city id={ny_weather.id}): \n" +
          f"Temperature: {ny_weather.temperature} \n" +
          f"Weather type: {ny_weather.weather_type}")

