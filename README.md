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

![c:\Users\Administrator\Pictures\Screenshots\ss1.png](Add screenshot 1 here with proper name)
Interface for fetc

![Screenshot2](Add screenshot 2 here with proper name)
*Add caption explaining what this shows*

![Screenshot3](Add screenshot 3 here with proper name)
*Add caption explaining what this shows*

#### Diagrams

**System Architecture:**

![Architecture Diagram](docs/architecture.png)
*Explain your system architecture - components, data flow, tech stack interaction*

**Application Workflow:**

![Workflow](docs/workflow.png)
*Add caption explaining your workflow*

---


#### Build Photos

![Team](Add photo of your team here)

![Components](Add photo of your components here)
*List out all components shown*

![Build](Add photos of build process here)
*Explain the build steps*

![Final](Add photo of final product here)
*Explain the final build*

---

## Additional Documentation

### For Web Projects with Backend:

#### API Documentation

**Base URL:** `https://api.yourproject.com`

##### Endpoints

**GET /api/endpoint**
- **Description:** [What it does]
- **Parameters:**
  - `param1` (string): [Description]
  - `param2` (integer): [Description]
- **Response:**
```json
{
  "status": "success",
  "data": {}
}
```

**POST /api/endpoint**
- **Description:** [What it does]
- **Request Body:**
```json
{
  "field1": "value1",
  "field2": "value2"
}
```
- **Response:**
```json
{
  "status": "success",
  "message": "Operation completed"
}
```

[Add more endpoints as needed...]

---





## AI Tools Used (Optional - For Transparency Bonus)

If you used AI tools during development, document them here for transparency:

**Tool Used:** [ChatGPT, Claude]

**Purpose:** [What you used it for]
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

*Note: Proper documentation of AI usage demonstrates transparency and earns bonus points in evaluation!*

---

## Team Contributions

- [Nourin Basheer K]: [Specific contributions -  Frontend development]
- [Thapasya E K]: [Specific contributions - Backend development]

---

## License

This project is licensed under the [LICENSE_NAME] License - see the [LICENSE](LICENSE) file for details.

**Common License Options:**
- MIT License (Permissive, widely used)
- Apache 2.0 (Permissive with patent grant)
- GPL v3 (Copyleft, requires derivative works to be open source)

---

Made with ❤️ at TinkerHub
