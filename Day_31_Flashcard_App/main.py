#from ui import *
#import random
from tkinter import *

MAIN_FILEPATH = "Day_31_Flashcard_App/"
BACKGROUND_COLOR = "#B1DDC6"

#generate_ui(IMG_FILEPATH=MAIN_FILEPATH+"images/card_front.png")

window = Tk()
window.title("English - French Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# create the main flashcard
canvas = Canvas(width=800, height=526)
canvas_img = PhotoImage(file = MAIN_FILEPATH+"images/card_front.png")
canvas.create_image(800/2,526/2, image=canvas_img)
canvas.create_text(400, 150, text="Title", font=("Arial",40,"italic"))
canvas.create_text(800/2,526/2,text="Word", font=("Arial",60,"bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=1,row=0)

#create buttons for the flashcard to indicate if user knows the answer or not



window.mainloop()


