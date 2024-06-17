"""This is the main application file that runs the server."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detecter

app = Flask("Emotion Detecter")

@app.route("/emotionDetector")
def sent_detecter():
    """
    Sends the user's input to the IBM Watson emotion detector
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detecter(text_to_analyze)

    if not response['dominant_emotion']:
        return "<b>Invalid text! Please try again!</b>"

    keys = ('anger', 'disgust', 'fear', 'joy')
    joined = ", ".join(["'"+key+"': "+str(response[key]) for key in keys])
    return (f"For the given statement, the system response is {joined} and "
            f"'sadness': {response['sadness']}. "
            f"The dominant emotion is <b>{response['dominant_emotion']}</b>.")

@app.route("/")
def render_index_page():
    """
    Renders the index page
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
