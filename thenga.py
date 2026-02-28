import streamlit as st
import joblib
import numpy as np
import requests

# Load model
model = joblib.load("fire_model.pkl")

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 1
if "weather_data" not in st.session_state:
    st.session_state.weather_data = None
if "inputs" not in st.session_state:
    st.session_state.inputs = {}

# Page config
st.set_page_config(page_title="🎇 Fireworks Risk Predictor", layout="wide")

# -------- Global CSS for background and styling --------
st.markdown("""
    <style>
    /* Full page background */
    body {
        background-color: #f0f4f8;
    }
    /* Heading box */
    .heading-box {
        background: linear-gradient(90deg, #ff6666, #ff9999);
        padding: 30px;
        border-radius: 40px;
        text-align: center;
        font-size: 50px;
        color: white;
        font-weight: bold;
        margin-bottom: 40px;
    }
    /* Weather boxes */
    .weather-box {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 30px;
        text-align: center;
        font-size: 24px;
        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
    }
    /* Scroll container for sliders */
    .slider-container {
        max-height: 300px;
        overflow-y: auto;
        padding-right: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# -------- Heading --------
st.markdown('<div class="heading-box">🎇 AI-Based Fireworks Risk Prediction</div>', unsafe_allow_html=True)

# -------- Step 1: City Input --------
if st.session_state.step == 1:
    city = st.text_input("Enter City Name", st.session_state.inputs.get("city", ""))
    
    if city:
        api_key = "654ea2a77ff59aca3ca5ba745084a8ec" #with your OpenWeatherMap key
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        
        if response.status_code == 200:
            weather_data = response.json()
            st.session_state.weather_data = weather_data
            st.session_state.inputs["city"] = city
        else:
            error_message = response.json().get("message", "Unknown error")
            st.error(f"Error: {error_message}")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.button("Next ➡️", on_click=lambda: st.session_state.__setitem__("step", 2))

# -------- Step 2: Display fetched weather data --------
elif st.session_state.step == 2:
    st.subheader("🌤 Weather Data")
    
    if st.session_state.weather_data:
        temperature = st.session_state.weather_data["main"]["temp"]
        humidity = st.session_state.weather_data["main"]["humidity"]
        wind_speed = st.session_state.weather_data["wind"]["speed"]
        
        # Store in session state
        st.session_state.inputs["temperature"] = temperature
        st.session_state.inputs["humidity"] = humidity
        st.session_state.inputs["wind_speed"] = wind_speed
        
        # Display in big rounded boxes
        col1, col2, col3 = st.columns(3)
        col1.markdown(f'<div class="weather-box">🌡 Temperature<br>{temperature} °C</div>', unsafe_allow_html=True)
        col2.markdown(f'<div class="weather-box">💧 Humidity<br>{humidity} %</div>', unsafe_allow_html=True)
        col3.markdown(f'<div class="weather-box">🌬 Wind Speed<br>{wind_speed} m/s</div>', unsafe_allow_html=True)
    else:
        st.info("Weather data not available. Please go back and enter a valid city.")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.button("⬅️ Previous", on_click=lambda: st.session_state.__setitem__("step", 1))
    with col2:
        st.button("Next ➡️", on_click=lambda: st.session_state.__setitem__("step", 3))

# -------- Step 3: Manual Inputs with scrolling sliders --------
elif st.session_state.step == 3:
    st.subheader("📊 Manual Inputs")
    
    st.markdown('<div class="slider-container">', unsafe_allow_html=True)
    st.session_state.inputs["crowd_size"] = st.slider("👥 Crowd Size", 0, 1000, st.session_state.inputs.get("crowd_size", 200))
    st.session_state.inputs["storage_days"] = st.slider("📦 Storage Duration (days)", 1, 30, st.session_state.inputs.get("storage_days", 5))
    st.session_state.inputs["quantity"] = st.slider("🎆 Fireworks Quantity (kg)", 10, 500, st.session_state.inputs.get("quantity", 100))
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1,1])
    with col1:
        st.button("⬅️ Previous", on_click=lambda: st.session_state.__setitem__("step", 2))
    with col2:
        st.button("Next ➡️", on_click=lambda: st.session_state.__setitem__("step", 4))

# -------- Step 4: Prediction --------
elif st.session_state.step == 4:
    st.subheader("📈 Prediction Result")
    
    input_data = np.array([[st.session_state.inputs["temperature"],
                            st.session_state.inputs["humidity"],
                            st.session_state.inputs["wind_speed"],
                            st.session_state.inputs["crowd_size"],
                            st.session_state.inputs["storage_days"],
                            st.session_state.inputs["quantity"]]])
    
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)
    
    if prediction == "Safe":
        st.success("🟢 SAFE")
    elif prediction == "Warning":
        st.warning("🟡 WARNING")
    else:
        st.error("🔴 HIGH RISK")
    
    st.write("Confidence:", round(np.max(probability)*100, 2), "%")
    
    col1, col2 = st.columns([1,1])
    with col1:
        st.button("⬅️ Previous", on_click=lambda: st.session_state.__setitem__("step", 3))
    with col2:
        st.button("🔄 Restart", on_click=lambda: st.session_state.__setitem__("step", 1))