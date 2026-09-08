# Emotion Detection Web Application

## Overview
This project is an AI-based web application that detects emotions from text input using IBM Watson NLP library. It analyzes customer feedback and identifies emotions like joy, sadness, anger, disgust, and fear.

## Features
- 🧠 Emotion detection using IBM Watson NLP API
- 🌐 RESTful API with Flask
- 🖥️ Web interface for user input
- ✅ Unit testing with `unittest`
- ⚠️ Error handling for invalid inputs
- 📊 Static code analysis with Pylint

## Project Structure

emotion-detection-app/
├── EmotionDetection/
│ ├── init.py
│ └── emotion_detection.py
├── tests/
│ └── test_emotion_detection.py
├── templates/
│ └── index.html
├── static/
│ └── mywebscript.js
├── server.py
├── README.md
└── .gitignore

## Technologies Used
- Python 3.x
- IBM Watson NLP
- Flask
- requests
- unittest
- Pylint

## Installation
```bash
# Clone the repository
git clone https://github.com/your-username/emotion-detection-app.git

# Navigate to the project directory
cd emotion-detection-app

# Install dependencies
python3 -m pip install flask requests

## Usage
# Run the Flask server
python3 server.py

# Access the application at http://127.0.0.1:5000

## API Endpoint
GET /emotionDetector?textToAnalyze=<text> - Returns emotion analysis

## Sample Output

```bash
For the given statement, the system response is 'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.9 and 'sadness': 0.0. The dominant emotion is joy.


## Running Tests
python3 -m unittest tests/test_emotion_detection.py

## Static Code Analysis
python3 -m pip install pylint
pylint EmotionDetection/emotion_detection.py
pylint server.py

