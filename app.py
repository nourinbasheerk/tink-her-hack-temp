import streamlit as st
import joblib
import numpy as np
import requests

model = joblib.load("fire_model.pkl")

st.title("🎇 AI-Based Fireworks Risk Prediction System")

# -------- City Input --------
city = st.text_input("Enter City Name")

weather_data = None

if city:
    api_key = "654ea2a77ff59aca3ca5ba745084a8ec"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()

        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        st.success(f"Weather data fetched for {city}")
        st.write("Temperature:", temperature, "°C")
        st.write("Humidity:", humidity, "%")
        st.write("Wind Speed:", wind_speed, "m/s")

    else:
        st.error("City not found")

# -------- Manual Inputs --------
crowd_size = st.slider("👥 Crowd Size", 0, 1000, 200)
storage_days = st.slider("📦 Storage Duration (days)", 1, 30, 5)
quantity = st.slider("🎆 Fireworks Quantity (kg)", 10, 500, 100)

# -------- Prediction --------
if st.button("Predict Risk") and weather_data:

    input_data = np.array([[temperature, humidity, wind_speed,
                            crowd_size, storage_days, quantity]])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)

    if prediction == "Safe":
        st.success("🟢 SAFE")
    elif prediction == "Warning":
        st.warning("🟡 WARNING")
    else:
        st.error("🔴 HIGH RISK")

    st.write("Confidence:", round(np.max(probability)*100, 2), "%")