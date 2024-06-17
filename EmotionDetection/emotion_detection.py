"""Module that wraps the IBM Watson functions."""

import requests
import json

def emotion_detecter(text_to_analyse):
   """
   Awesome function that does IBM Watson things
   """
   url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
   myobj = { "raw_document": { "text": text_to_analyse } }
   header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
   response = requests.post(url, json = myobj, headers=header)

   if response.status_code == 400:
      return {'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
        }

   values = json.loads(response.text)
   emotions = values['emotionPredictions'][0]['emotion']
   highest, h_key = 0, None
   for key, value in emotions.items():
      if value > highest:
        highest = value
        h_key = key

   return {
    'anger': emotions['anger'],
    'disgust': emotions['disgust'],
    'fear': emotions['fear'],
    'joy': emotions['joy'],
    'sadness': emotions['sadness'],
    'dominant_emotion': h_key
    }