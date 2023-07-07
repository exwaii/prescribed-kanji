import requests
import json
import urllib.parse
import dotenv
import os

dotenv.load()

api_key = os.getenv("API_KEY")


with open('kanji.txt', 'r', encoding="utf-8") as f:
    kanji_list = f.read().splitlines()

data_list = []

for kanji in kanji_list:
    r = requests.get(
        url=f"https://kanjialive-api.p.rapidapi.com/api/public/kanji/{urllib.parse.quote(kanji)}",
        headers={
            'X-RapidAPI-Key': api_key,
            'X-RapidAPI-Host': 'kanjialive-api.p.rapidapi.com'
        }
    ).json()
    data_list.append(
        {
            "kanji": kanji,
            "kun": r["kunyomi_ja"],
            "on": r["onyomi_ja"],
            "meaning": r["meaning"],
        }
    )
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data_list, f, indent=4, ensure_ascii=False)
