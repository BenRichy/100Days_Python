from tkinter import *

def button_clicked():
    my_label["text"] = input.get()
    print("I got clicked")

#create window
window = Tk()
window.title("First GUI program")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

# create label
my_label = Label(text = "This is a label",
                         font = ("Arial",24,"bold"))
# call pack, place or grid to put it on the screen
my_label.grid(column=0,row=0)

my_label["text"] = "New text"

# button
button = Button(text = "Click me", command=button_clicked)
button.grid(column=1,row=1)

# entry
input = Entry(width = 10)
input.grid(column=3,row=3)

# new button
new_button = Button(text="New button")
new_button.grid(column=2,row=0)

#keep window open; has to be at end
window.mainloop()