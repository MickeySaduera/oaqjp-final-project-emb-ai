from flask import Flask, request, render_template, Response
import json
import sys
sys.path.append('/home/project/final_project/oaqjp-final-project-emb-ai/EmotionDetection')
from emotion_detection import emotion_detector 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotionDetector():
    text_to_analyze = request.args.get('textToAnalyze', '')

    # emotion_detector returns a dict, so no need to json.loads
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