#import libraries
import random
from tkinter import *
import pandas as pd

MAIN_FILEPATH = "Day_31_Flashcard_App/"
BACKGROUND_COLOR = "#B1DDC6"

#Possible functionality to add
## Add a reset button to start again by deleting the to_learn file
## Add way of selecting flashcards to use from a set
## on start up, say how long you want before it flips

#read in csv data, and convert to each line to a dictionary
try:
    words_fr_en = pd.read_csv(MAIN_FILEPATH+"data/words_to_learn_fr_en.csv")
except FileNotFoundError:
    words_fr_en = pd.read_csv(MAIN_FILEPATH+"data/french_words.csv")
    words_fr_en.to_csv(MAIN_FILEPATH+"data/words_to_learn_fr_en.csv")

dict_fr_en= words_fr_en.to_dict(orient="records")
current_card = {}



def next_card():
    global current_card, flip_timer
    #when a new card is selected, reset the flip timer
    window.after_cancel(flip_timer)
    #choose a random word from the dictionary, and show it on the card
    current_card = random.choice(dict_fr_en)
    canvas.itemconfig(card_background, image = canvas_img_front)
    canvas.itemconfig(card_title, text = "French", fill="black")
    canvas.itemconfig(card_word, text = current_card["French"], fill="black")
    #reinstate the flip timer
    flip_timer = window.after(3000, flip_card)
    


def flip_card():
    global flip_timer
    #after 3000ms (3s) flip the card to show the meaning in english
    canvas.itemconfig(card_title, text = "English", fill="white")
    canvas.itemconfig(card_word, text = current_card["English"],fill="white")
    canvas.itemconfig(card_background, image = canvas_img_back)
    next

#if the meaning is known, then remove the word from the list
def is_known():
    dict_fr_en.remove(current_card)
    new_to_learn = pd.DataFrame(dict_fr_en)
    new_to_learn.to_csv(MAIN_FILEPATH+"data/words_to_learn_fr_en.csv", index=False)
    next_card()
    


window = Tk()
window.title("English - French Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# create the main flashcard
canvas = Canvas(width=800, height=526)
canvas_img_front = PhotoImage(file = MAIN_FILEPATH+"images/card_front.png")
canvas_img_back = PhotoImage(file = MAIN_FILEPATH+"images/card_back.png")
card_background = canvas.create_image(800/2,526/2, image=canvas_img_front)
card_title = canvas.create_text(400, 150, text="", font=("Arial",40,"italic"))
card_word = canvas.create_text(800/2,526/2,text="", font=("Arial",60,"bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0,row=0, columnspan=2)

#create buttons for the flashcard to indicate if user knows the answer or not
img_wrong = PhotoImage(file = MAIN_FILEPATH+"images/wrong.png")
button_wrong = Button(image=img_wrong, highlightthickness=0, command=next_card)
button_wrong.grid(column=0,row=1)

img_correct = PhotoImage(file = MAIN_FILEPATH+"images/right.png")
button_correct = Button(image=img_correct, highlightthickness=0, command=is_known)
button_correct.grid(column=1,row=1)

next_card()


window.mainloop()


