# flashCards.py
#
# Python Bootcamp Day 30 - Flash Cards
# Usage:
# The program defaults to Spanish words, but you can also use a French
# dictionary. The foreign word will be shown for 3 seconds, then it's English
# translation will be shown. If you know the word, click the green checkmark
# button and the word will be removed from the dictionary. Click the red X and
# the deck will be reshuffled and you'll be shown a new card.
#
# If you want to use a new dictionary, change:
#
# words = pd.read_csv("data/spanish_words.csv") to correct csv and find/replace
# "Spanish" to new column head in csv (eg. "French", "German", etc)
#
# Marceia Egler November 30, 2021
import sys
from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
foreign_word = {}

try:
    words = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    words = pd.read_csv("data/spanish_words.csv")

to_learn = words.to_dict(orient="records")

# ------------------------- PICK NEW CARD ------------------------------- #
def new_card():
    global foreign_word, flip_timer
    window.after_cancel(flip_timer)
    foreign_word = random.choice(to_learn)
    canvas.itemconfig(title, text="Spanish", fill="black")
    canvas.itemconfig(new_word, text=foreign_word["Spanish"], fill="black")
    canvas.itemconfig(front, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(front, image=card_back_img)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(new_word, text=foreign_word["English"], fill="white")


def remove_card():
    idx = words.index[words["Spanish"] == foreign_word["Spanish"]]
    words.drop(idx, axis=0, inplace=True)
    words.to_csv("data/words_to_learn.csv", index=False)
    new_card()


# -------------------------- UI LAYOUT ---------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526)

# Card Front
card_front_img = PhotoImage(file="images/card_front.png")
# Card Back
card_back_img = PhotoImage(file="images/card_back.png")

front = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
new_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(
    image=cross_img, command=new_card, highlightthickness=0
)
unknown_button.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
known_button = Button(
    image=check_img, command=remove_card, highlightthickness=0
)
known_button.grid(row=1, column=1)

# ------------------------- RUN FLASH CARDS ----------------------------- #

new_card()

window.mainloop()
