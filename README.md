# Foreign Language Flash Cards

A foreign language frequentyly used words application using tkinter. 
Day 31 Python Bootcamp


## Usage
The program defaults to Spanish words, but you can also use a French dictionary.
The foreign word will be shown for 3 seconds, then it's English translation will
be shown. If you know the word, click the green checkmark button and the word
will be removed from the dictionary. Click the red X and the deck will be 
reshuffled and you'll be shown a new card.

If you want to use a new dictionary, change Line 28:

    words = pd.read_csv("data/spanish_words.csv") 
    
to correct csv and find/replace "Spanish" to new column head in csv
(eg. "French", "German", etc)

## License
[MIT](https://choosealicense.com/licenses/mit/)