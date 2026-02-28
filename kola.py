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

# -------- Global CSS for green theme and slider --------
st.markdown("""
<style>
/* Page background */
body, .stApp {
    background-color: #d0f0c0;  /* pastel green page background */
}

/* Heading box */
.heading-box {
    background-color: #90ee90;  /* light green */
    padding: 40px;
    border-radius: 50px;
    text-align: center;
    font-size: 50px;
    color: #000000;
    font-weight: bold;
    margin-bottom: 40px;
    width: 90%;
    margin-left: auto;
    margin-right: auto;
}

/* Weather boxes with white border */
.weather-box {
    background-color: #90ee90;  /* light green */
    padding: 25px;
    border-radius: 30px;
    text-align: center;
    font-size: 24px;
    color: #000000;
    margin-bottom: 20px;
    border: 5px solid #ffffff;  /* thick white border */
    box-shadow: 2px 2px 15px rgba(0,0,0,0.2);
}

/* Manual input heading */
.manual-heading {
    background-color: #90ee90;
    color: black;
    font-size: 36px;
    padding: 25px;
    border-radius: 30px;
    text-align: center;
    margin-bottom: 25px;
}

/* Each manual input title smaller */
.manual-input-title {
    background-color: #c0f0a0;  /* slightly lighter green */
    color: black;
    font-size: 18px;  /* smaller font */
    padding: 10px;    /* smaller box */
    border-radius: 15px;
    margin-top: 10px;
    margin-bottom: 10px;
    text-align: center;
}

/* Slider track styling */
.css-1v3fvcr {  /* targets slider track */
    background-color: #32cd32 !important;  /* lime green track */
    height: 20px !important;
    border-radius: 10px;
}

/* Slider knob styling */
.css-1u7zfla {  /* knob */
    background-color: white !important;
    border: 2px solid #228B22 !important;  /* dark green border */
}

/* Slider value text */
.css-1gex4x5 {  /* value bubble text */
    color: black !important;
    font-weight: bold;
}

/* Buttons */
.stButton>button {
    background-color: #90ee90;
    color: black;
    font-size: 18px;
    padding: 10px 25px;
    border-radius: 15px;
}

/* Text input bigger */
.stTextInput>div>input {
    font-size: 24px !important;
    height: 50px !important;
    color: #000000;
    padding-left: 10px;
}
</style>
""", unsafe_allow_html=True)

# -------- Heading --------
st.markdown('<div class="heading-box">🎇 AI-Based Fireworks Risk Prediction</div>', unsafe_allow_html=True)

# -------- Step 1: City Input --------
if st.session_state.step == 1:
    city = st.text_input("Enter City Name", st.session_state.inputs.get("city", ""),
                         placeholder="Type your city here...", key="city_input", label_visibility="visible")

    if city:
        api_key = "722146f736cd86d7c5b5f12aa4153cdf"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            st.session_state.weather_data = weather_data
            st.session_state.inputs["city"] = city
        else:
            error_message = response.json().get("message", "Unknown error")
            st.error(f"Error: {error_message}")

    st.markdown('<div style="margin-top:50px; text-align:right;">', unsafe_allow_html=True)
    st.button("Next ➡️", on_click=lambda: st.session_state.__setitem__("step", 2))
    st.markdown('</div>', unsafe_allow_html=True)

# -------- Step 2: Weather Data --------
elif st.session_state.step == 2:
    st.subheader("🌤 Weather Data")
    
    if st.session_state.weather_data:
        temperature = st.session_state.weather_data["main"]["temp"]
        humidity = st.session_state.weather_data["main"]["humidity"]
        wind_speed = st.session_state.weather_data["wind"]["speed"]
        
        st.session_state.inputs["temperature"] = temperature
        st.session_state.inputs["humidity"] = humidity
        st.session_state.inputs["wind_speed"] = wind_speed
        
        col1, col2, col3 = st.columns(3)
        col1.markdown(f'<div class="weather-box">🌡 Temperature<br>{temperature} °C</div>', unsafe_allow_html=True)
        col2.markdown(f'<div class="weather-box">💧 Humidity<br>{humidity} %</div>', unsafe_allow_html=True)
        col3.markdown(f'<div class="weather-box">🌬 Wind Speed<br>{wind_speed} m/s</div>', unsafe_allow_html=True)
    else:
        st.info("Weather data not available. Please go back and enter a valid city.")

    col1, col2 = st.columns([1,1])
    with col1:
        st.button("⬅️ Previous", on_click=lambda: st.session_state.__setitem__("step", 1))
    with col2:
        st.button("Next ➡️", on_click=lambda: st.session_state.__setitem__("step", 3))

# -------- Step 3: Manual Inputs --------
elif st.session_state.step == 3:
    st.markdown('<div class="manual-heading">📊 Manual Inputs</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="slider-container">', unsafe_allow_html=True)

    st.markdown('<div class="manual-input-title">👥 Crowd Size</div>', unsafe_allow_html=True)
    st.session_state.inputs["crowd_size"] = st.slider("", 0, 1000, st.session_state.inputs.get("crowd_size", 200))

    st.markdown('<div class="manual-input-title">📦 Storage Duration (days)</div>', unsafe_allow_html=True)
    st.session_state.inputs["storage_days"] = st.slider("", 1, 30, st.session_state.inputs.get("storage_days", 5))

    st.markdown('<div class="manual-input-title">🎆 Fireworks Quantity (kg)</div>', unsafe_allow_html=True)
    st.session_state.inputs["quantity"] = st.slider("", 10, 500, st.session_state.inputs.get("quantity", 100))

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