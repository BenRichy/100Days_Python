from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    # from day 5 of this course

    # lists of letters, numbers and symbols to use
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # define number of characters to use
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)

    # insert password to manager tool
    entry_password.insert(0, password)

    # copy generated password to clipboard
    pyperclip.copy(password)





# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    # obtain user inputs
    write_website = entry_website.get()
    write_email = entry_email.get()
    write_password = entry_password.get()

    # create string to output to json file
    json_output = {
        write_website: {
            "email": write_email,
            "password": write_password
        }
    }



    # create messagebox to inform user if any fields are empty
    if len(write_website) == 0 or len(write_password) == 0:
        messagebox.showwarning(title="Warning!",
                               message="Oops! Please don't leave any fields blank!")

    else:
        # create messagebox so user can confirm whether details are correct or not
        is_ok = messagebox.askokcancel(title=write_email,
                                       message=f"These are the details:\nEmail: {write_email}\nPassword: {write_password}\nIs it okay to save?")

        if is_ok:

            try:
                # open and edit file
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(json_output)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(json_output, data_file, indent=4)
            else:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                # clear website and password entry after add an account
                entry_website.delete(0,END)
                entry_password.delete(0, END)

                # put cursor back in website
                entry_website.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)



canvas = Canvas(width=200,
                height=200)

pw_lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pw_lock_img)
canvas.grid(column=1,row=0)

#Labels
label_website = Label(text="Website:")
label_website.grid(column=0,row=1)

label_email = Label(text="Email/Username:")
label_email.grid(column=0,row=2)

label_password = Label(text = "Password:")
label_password.grid(column=0,row=3)

#Entries
entry_website = Entry(width=50)
entry_website.grid(column=1,row=1,columnspan=2)

entry_email = Entry(width=50)
entry_email.grid(column=1,row=2,columnspan=2)

entry_password = Entry(width=30)
entry_password.grid(column=1,row=3)

#Buttons
button_generate = Button(text="Generate Password", width = 16, command = generate_password)
button_generate.grid(column=2,row=3)

button_add = Button(width=36,text="Add", command=save_password)
button_add.grid(column=1,row=4,columnspan=2)

#Set Up
## Put cursor in website
entry_website.focus()
entry_email.insert(0,"ben@email.co.uk")

window.mainloop()

