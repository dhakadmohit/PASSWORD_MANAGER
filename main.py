from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_credential():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Make sure you haven't left any field empty\n")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# .....................................................................
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP -------------------------------
window = Tk()
window.config(height=220,width=220,padx=50,pady=50)
window.title("Password Manager")

canvas = Canvas(width=200,height=200)
logo_image = PhotoImage(file="D:/Python VS CODE/PASSWORD_MANAGER/logo.png") 
canvas.create_image(100,100,image= logo_image)
canvas.grid(row=0,column=1)
# .................................................................................

#LABELS
website_label = Label(text="Website")
website_label.grid(column=0,row=1)
Email_label = Label(text="Email/Username")
Email_label.grid(column=0,row=2)
Password_label = Label(text="Password")
Password_label.grid(column=0,row=3)
# ..................................................................................

# BUTTONS
Genrate_button = Button(text="Generate Password",highlightthickness=0,command=generate_password)
Genrate_button.grid(column=2,row=3)
add_button = Button(text="Add",width=42,highlightthickness=0,command=save_credential)
add_button.grid(column=1,row=4,columnspan=2)
search_button = Button(text="Search",highlightthickness=0,width=14,command=find_password)
search_button.grid(row=1,column=2)
# ..................................................................................

# ENTRY
website_entry = Entry()
website_entry.focus()
website_entry.config(width=32)
website_entry.grid(row=1,column=1)
email_entry = Entry()
email_entry.config(width=50)
email_entry.insert(0, "xyz@gmail.com")
email_entry.grid(row=2,column=1,columnspan=2)
password_entry = Entry(width=32)
password_entry.grid(row=3,column=1)
# ..................................................................................

window.mainloop()