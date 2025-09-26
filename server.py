"""
server.py - Flask web server for Emotion Detection application.
"""
from flask import Flask, request, render_template, Response
from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)

def emotion_detector_wrapper(text_to_analyze):
    """
    Calls the emotion_detector function and processes the response.
    Handles invalid input and errors gracefully.

    Args:
        text_to_analyze (str): Text to analyze for emotions.

    Returns:
        None values if input is invalid or an error occurs.
    """
    try:
        response = emotion_detector(text_to_analyze)

        if hasattr(response, 'status_code') and response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }


    except (AttributeError, TypeError) as e:
        print(f"Handled error in emotion_detector: {e}")


    return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

@app.route('/')
def home():
    """
    Use template for index
    """
    return render_template('index.html')


@app.route('/emotionDetector', methods=['GET'])
def emotiondetect():
    """
    Process user input from text
    """
    text_to_analyze = request.args.get('textToAnalyze', '').strip()

    if not text_to_analyze:
        response_str = "Invalid text! Please try again!\nResponse: None"
        return Response(response_str, mimetype='text/plain')

    result_dict = emotion_detector(text_to_analyze)

    response_str = (
        f"For the given statement, the system response is "
        f"'anger': {result_dict['anger']}, "
        f"'disgust': {result_dict['disgust']}, "
        f"'fear': {result_dict['fear']}, "
        f"'joy': {result_dict['joy']} and "
        f"'sadness': {result_dict['sadness']}. "
        f"The dominant emotion is {result_dict['dominant_emotion']}."
    )

    return Response(response_str, mimetype='text/plain')


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
