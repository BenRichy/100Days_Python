from tkinter import *
from tkinter import messagebox

def generate_ui(BACKGROUND_COLOR = "#B1DDC6", IMG_FILEPATH=""):
    window = Tk()
    window.title("English - French Flashcards")
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

    canvas = Canvas(width=800, height=528)
    canvas_img = PhotoImage(file = IMG_FILEPATH)
    canvas.create_image(800/2,528/2, image=canvas_img)
    canvas.config(bg=BACKGROUND_COLOR)
    canvas.grid(column=1,row=0)

    window.mainloop()


