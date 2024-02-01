import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric' 
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: Unable to fetch weather data. Status Code: {response.status_code}")
        return None

def display_weather(data):
    if data:
        print(f"Weather in {data['name']}, {data['sys']['country']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Weather Conditions: {data['weather'][0]['description']}")
    else:
        print("Weather data not available.")

if __name__ == "__main__":
    api_key = "Your_Weather_API_Key" #make sure to sign up for a free API key from OpenWeatherMap: https://openweathermap.org/appid

    while True:
        location = input("Enter city or ZIP code (or 'exit' to quit): ")

        if location.lower() == 'exit':
            break

        weather_data = get_weather(api_key, location)

        if weather_data:
            display_weather(weather_data)
