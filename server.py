"""
Flask server for Emotion Detection web application.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the home page with the emotion detection form.
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_route():
    """
    Handle GET requests to analyze emotions from text input.
    """
    # Get the text to analyze from the query parameter
    text_to_analyze = request.args.get('textToAnalyze', '')

    # Validate input
    if not text_to_analyze or text_to_analyze.strip() == '':
        return "Invalid text! Please try again."

    # Call the emotion_detector function
    result = emotion_detector(text_to_analyze)

    # Check if the result contains valid emotions
    if result.get('dominant_emotion') is None:
        return "Invalid text! Please try again."

    # Format the output as required
    output = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return output

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)