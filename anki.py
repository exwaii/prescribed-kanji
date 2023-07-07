import requests
import json


# AnkiConnect helper function
def invoke(action, **params):
    request_json = json.dumps(
        {'action': action, 'params': params, 'version': 6})
    response = json.loads(requests.post(
        'http://localhost:8765', data=request_json).content)
    if len(response) != 2:
        raise Exception(
            'AnkiConnect returned an incorrect number of response elements.')
    if 'error' not in response:
        raise Exception('AnkiConnect is missing required error field.')
    if 'result' not in response:
        raise Exception('AnkiConnect is missing required result field.')
    if response['error'] is not None:
        raise Exception(response['error'])
    return response['result']


deck_name = "Prescribed Kanji"
model_name = "prescribed-kanji"

invoke("createDeck", deck=deck_name)

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

data = [
    {
        "deckName": deck_name,
        "modelName": model_name,
        "fields": {
            "kanji": kanji["kanji"],
            "kunyomi": kanji['kun'],
            "onyomi": kanji['on'],
            "meaning": kanji['meaning'],
        },
    }
    for kanji in data
]

invoke("addNotes", notes=data)
