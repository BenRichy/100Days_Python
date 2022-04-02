# packages
from tkinter import *

def convert_distance():
    miles_dist = float(input_miles.get())
    km_dist = str(miles_dist * 1.6)
    label_result_km["text"] = km_dist

#create window
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=100)

# create miles entry
input_miles = Entry(width = 10)
input_miles.grid(column=1,row=0)

# add text to app
label_miles = Label(text = "Miles",
                         font = ("Arial",24,"bold"))
label_equiv = Label(text = "is equal to",
                         font = ("Arial",24,"bold"))
label_km = Label(text = "Km",
                         font = ("Arial",24,"bold"))
label_result_km = Label(text = "0",
                         font = ("Arial",24,"bold"))

## arrange text
label_miles.grid(column=2,row=0)
label_equiv.grid(column=0,row=1)
label_km.grid(column=2,row=1)
label_result_km.grid(column=1,row=1)

# button to convert data
button_convert = Button(text = "Calculate", command=convert_distance)
button_convert.grid(column=1,row=2)


#keep window open; has to be at end
window.mainloop()