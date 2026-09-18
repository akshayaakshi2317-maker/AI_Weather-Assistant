import streamlit as st
from weather_functions import get_weather


st.set_page_config(
    page_title="AI Weather Assistant",
    page_icon="🌤️"
)

st.title("🌤️ AI Weather Assistant")
st.write("Weather application using Open-Meteo API")


user_input = st.chat_input(
    "Example: What is the weather in Chennai?"
)


if user_input:

    st.write("You entered:", user_input)

    words = user_input.split()

    if "in" in words:

        index = words.index("in")

        if index + 1 < len(words):

            city = " ".join(
                words[index + 1:]
            ).strip("?.!,")

            result = get_weather(city)

            if "error" in result:

                st.error(result["error"])

            else:

                weather_code = result["weather_code"]

                weather_description = {
                    0: "Clear sky",
                    1: "Mainly clear",
                    2: "Partly cloudy",
                    3: "Overcast",
                    45: "Fog",
                    48: "Fog",
                    51: "Light drizzle",
                    53: "Moderate drizzle",
                    55: "Dense drizzle",
                    61: "Slight rain",
                    63: "Moderate rain",
                    65: "Heavy rain",
                    80: "Rain showers",
                    81: "Rain showers",
                    82: "Heavy rain showers",
                    95: "Thunderstorm"
                }

                description = weather_description.get(
                    weather_code,
                    "Unknown weather"
                )

                st.subheader(
                    f"🌤️ Weather in {result['city']}, {result['country']}"
                )

                st.write(
                    f"☁️ **Condition:** {description}"
                )

                st.write(
                    f"🌡️ **Temperature:** {result['temperature']} °C"
                )

                st.write(
                    f"🌡️ **Feels Like:** {result['feels_like']} °C"
                )

                st.write(
                    f"💧 **Humidity:** {result['humidity']}%"
                )

                st.write(
                    f"🌬️ **Wind Speed:** {result['wind_speed']} km/h"
                )

                st.write(
                    f"🌧️ **Precipitation:** {result['precipitation']} mm"
                )

        else:

            st.warning("Please enter a city name.")

    else:

        st.warning(
            "Please type like: What is the weather in Chennai?"
        )