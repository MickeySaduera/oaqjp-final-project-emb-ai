from flask import Flask, request, render_template, Response
import json
import sys
sys.path.append('/home/project/final_project/oaqjp-final-project-emb-ai/EmotionDetection')
from emotion_detection import emotion_detector 

app = Flask(__name__)

def emotion_detector(text_to_analyze):
    try:
        
        response = call_emotion_detection_api(text_to_analyze)  

        if response.status_code == 400:
            
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

        
        result = process_response(response.text)  
        return result

    except Exception as e:
        print(f"Error in emotion_detector: {e}")
        
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
    return render_template('index.html')


@app.route('/emotionDetector', methods=['GET'])
def emotionDetector():
    text_to_analyze = request.args.get('textToAnalyze', '')

    result_dict = emotion_detector(text_to_analyze)

    if result_dict['dominant_emotion'] is None:
        response_str = (
            "Invalid text! Please try again!\n"
            f"Response: {result_dict}"
        )
    else:
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