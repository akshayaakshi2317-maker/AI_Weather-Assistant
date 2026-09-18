#  AI Weather Assistant

A simple weather application built using **Python, Streamlit, and Open-Meteo API**.

The application allows users to enter a city name and displays the current weather information such as temperature, humidity, feels-like temperature, wind speed, precipitation, and weather condition.

##  Features

*  Get current weather information
*  Display temperature
*  Display feels-like temperature
*  Display humidity
*  Display wind speed
*  Display precipitation
*  Display weather condition
*  Automatically finds the city coordinates
*  Simple Streamlit chat interface
*  Uses the Open-Meteo API

##  Technologies Used

* Python
* Streamlit
* Requests
* Open-Meteo API

##  Project Structure

```text
Function_Calling_Weather/
│
├── app.py
├── weather_functions.py
├── requirements.txt
├── README.md
└── screenshots/
```

##  How It Works

```text
User
  ↓
Streamlit Chat Interface
  ↓
Enter City
  ↓
app.py
  ↓
weather_functions.py
  ↓
Open-Meteo Geocoding API
  ↓
Get Latitude & Longitude
  ↓
Open-Meteo Weather API
  ↓
Get Current Weather
  ↓
Display Weather Information
```


##  Weather Information Displayed

The application displays:

* **Condition**
* **Temperature**
* **Feels Like**
* **Humidity**
* **Wind Speed**
* **Precipitation**

##  API Used

This project uses the **Open-Meteo API** to retrieve geocoding and weather information.

No API key is required for the free Open-Meteo usage used in this educational project.


##  Project Objective

The objective of this project is to build a simple weather assistant using **Streamlit** and the **Open-Meteo Weather API**, while learning how a Python application can communicate with an external API and display the returned data.

