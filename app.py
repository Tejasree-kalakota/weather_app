import streamlit as st
import requests

API_KEY = "1dc0c915814cefce0ce2f4ab6c4ff5dc"  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        resp = requests.get(BASE_URL, params=params, timeout=10)
        data = resp.json()
        if resp.status_code != 200:
            return None, data.get("message", "Error fetching data")
        return data, None
    except requests.exceptions.RequestException:
        return None, "Network error. Please check your internet."

# Streamlit UI
st.set_page_config(page_title="Weather App", page_icon="🌦", layout="centered")

st.title("🌦 Weather App")
st.write("Enter a city name to get the current weather.")

city = st.text_input("City Name")

if st.button("Get Weather"):
    if city.strip():
        weather_data, error = get_weather(city)
        if error:
            st.error(error)
        else:
            location = f"{weather_data['name']}, {weather_data['sys']['country']}"
            temp = weather_data['main']['temp']
            feels_like = weather_data['main']['feels_like']
            humidity = weather_data['main']['humidity']
            pressure = weather_data['main']['pressure']
            wind_speed = weather_data['wind']['speed']
            description = weather_data['weather'][0]['description'].title()

            st.subheader(location)
            st.write(f"**Condition:** {description}")
            st.write(f"**Temperature:** {temp}°C (Feels like {feels_like}°C)")
            st.write(f"**Humidity:** {humidity}%")
            st.write(f"**Pressure:** {pressure} hPa")
            st.write(f"**Wind Speed:** {wind_speed} m/s")
    else:
        st.warning("Please enter a city name.")
