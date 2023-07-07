# prescribed kanji anki deck

Based on the [2000 Japanese continuers prescribed kanji](https://educationstandards.nsw.edu.au/wps/wcm/connect/9a323ddb-dc9a-4e19-8142-5a896062e70e/japanese-continuers-vocab.pdf?MOD=AJPERES&CVID=) (last page)

`Prescribed Kanji.apkg` is the Anki deck, the rest of the files is code used to generate the deck.

`kanji.txt` contains linebreaked list of prescribed kanji.

`kanji.py` reads from `kanji.txt` and uses the [Kanji alive](https://kanjialive.com/) api to get the kanji's kunyomi and onyomi readings, as well as its meaning. This is written to `kanji.json`.

Note that you need an api key to use the Kanji alive api ([here](https://app.kanjialive.com/api/docs))

`anki.py` generates the anki deck from `kanji.json`.
