<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# [AI BASED FIREWORKS RISK PREDICTION] 🎯

## Basic Details

### Team Name: [Letz Code]

### Team Members
- Member 1: [Nourin Basheer K] - [TKM College of Engineering]
- Member 2: [Thapasya E K] - [TKM College of Engineering]

### Hosted Project Link
[mention your project hosted link here]

### Project Description
[This project is a Streamlit-based web app that predicts the risk level of fireworks events using a combination of real-time weather data and manual inputs such as crowd size, storage duration, and fireworks quantity.The app helps event organizers make safer decisions by classifying events as Safe, Warning, or High Risk with a confidence score.]

### The Problem statement
[Fireworks events can be dangerous due to factors like weather conditions, crowd size, improper storage, and the amount of fireworks used. Event organizers often rely on manual judgment, which can lead to accidents or unsafe situations.]

### The Solution
[The website collects real-time weather data from OpenWeather API (temperature, humidity, wind speed) and combines it with manual inputs such as crowd size, storage duration, and fireworks quantity. The model then classifies the event as Safe, Warning, or High Risk and provides a confidence score, helping organizers make informed and safer decisions.]

---

## Technical Details

### Technologies/Components Used

**For Software:**
- Languages used: [Python ] 
- Frameworks used: [Streamlit ]
- Libraries used: [numpy, joblib, requests, python-dotenv]
- Tools used: [VS Code, Git, Github]


---

## Features

- **Multi-Step User Interface:** Enter city, fetch weather data, input manual parameters, and view predictions step by step.  
- **Real-Time Weather Integration:** Fetches temperature, humidity, and wind speed from the OpenWeather API for accurate predictions.  
- **Manual Inputs:** Customize crowd size, storage duration, and fireworks quantity using intuitive sliders.  
- **AI-Powered Risk Prediction:** Classifies events as Safe, Warning, or High Risk with a confidence score to assist decision-making.  
- **Professional and Responsive UI:** Rounded boxes, sliders, and color themes for a modern, user-friendly experience.  
- **Secure API Handling:** Uses a `.env` file to store API keys safely, avoiding exposure on GitHub.

---

## Implementation

### For Software:

#### Installation
```bash
[Installation commands -# Install Streamlit for building the web app
pip install streamlit

# Install NumPy for array handling
pip install numpy

# Install Joblib for loading the ML model
pip install joblib

# Install Requests for API calls to OpenWeather
pip install requests

# Install python-dotenv to load environment variables (like API keys)
pip install python-dotenv]
```

#### Run
```bash
[Run commands - # Navigate to your project folder first
cd path/to/your/project

# Run the Streamlit app
streamlit run app.py]
```
---

## Project Documentation

### For Software:

#### Screenshots (Add at least 3)

<img width="1806" height="811" alt="ss1" src="https://github.com/user-attachments/assets/ce72e5c3-df4f-4013-81f4-91fabef477a8" />
Opening interface.The city name is fetched here

<img width="1837" height="797" alt="ss2" src="https://github.com/user-attachments/assets/f0e3b26f-b729-4637-94e7-de492522b9ee" />

The real time temperature,humidity and wind speed of the selected city is displayed here 

<img width="1731" height="866" alt="ss3" src="https://github.com/user-attachments/assets/09d3388a-9727-440f-a3a8-20f18be2fc8d" />

manual inputs like crowd density,quantity of fireworks 

<img width="1805" height="795" alt="ss4" src="https://github.com/user-attachments/assets/9b14d677-5312-46ea-bb48-5cc4e21f4a52" />

Result is displayed here.we can find whether its safe,warning or high risk
#### Diagrams

**System Architecture:**

<img width="575" height="840" alt="systemarchi" src="https://github.com/user-attachments/assets/013506bb-766d-4cfe-a054-b1eea95052da" /> Fireworks Risk Prediction – System Architecture
This diagram illustrates the technical structure of the system. The user interacts with the Streamlit interface, which sends a request to the OpenWeather API to retrieve weather data. The system then combines weather data and manual inputs to form a feature vector. This feature vector is passed to the trained machine learning model (fire_model.pkl), which produces the final risk classification along with a confidence score.


**Application Workflow:**

<img width="600" height="851" alt="ss5" src="https://github.com/user-attachments/assets/2d73eb5f-5e83-48cd-a4d7-4b239e95d0b9" />
Fireworks Risk Prediction – Workflow
This diagram shows the step-by-step process of the application. The user first enters a city name and fetches real-time weather data. Then, environmental parameters (temperature, humidity, wind speed) are collected and displayed. After that, the user provides manual inputs such as crowd size, storage duration, and fireworks quantity. Finally, all inputs are processed by the machine learning model to generate a risk prediction: Safe, Warning, or High Risk.



---

## Additional Documentation

### For Web Projects with Backend:

#### API Documentation

**Base URL:** `https://api.yourproject.com`

##### Endpoints

**GET /api/endpoint**
- **Description:** Name of the city to fetch weather
- **Parameters:**city
  - 
- **Response:**
{
  "status": "success",
  "data": {
    "temperature": 28.5,
    "humidity": 65,
    "wind_speed": 5.4,
    "city": "Mumbai"
  }
}
{
  "status": "error",
  "message": "City not found"
}
**POST /api/endpoint**
- **Description:** Predict fireworks risk based on weather data and manual inputs (crowd size, storage duration, fireworks quantity
- **Request Body:**
{
  "temperature": 28.5,
  "humidity": 65,
  "wind_speed": 5.4,
  "crowd_size": 200,
  "storage_days": 5,
  "quantity": 100
}
- **Response:**


{
  "status": "success",
  "prediction": "Safe",
  "confidence": 92.5
}

{
  "status": "error",
  "message": "Missing required input(s)"
}



## AI Tools Used (Optional - For Transparency Bonus)

If you used AI tools during development, document them here for transparency:

**Tool Used:** [ChatGPT, Claude]

**Purpose:** 
-  "Generated code"
-  "Debugging functions"
-  "Code review and optimization suggestions"

**Key Prompts Used:**
- "Create dataset"
- "Create a streamlit interface for fireworks safety"
- "Debug this code"


**Percentage of AI-generated code:** [Approximately 98%]

**Human Contributions:**
- Architecture design and planning
- UI/UX design decisions


## Team Contributions

- [Nourin Basheer K]: [Specific contributions -  Frontend development]
- [Thapasya E K]: [Specific contributions - Backend development]

---

## License

- MIT License (Permissive, widely used)
- Apache 2.0 (Permissive with patent grant)
- GPL v3 (Copyleft, requires derivative works to be open source)

---

Made with ❤️ at TinkerHub
