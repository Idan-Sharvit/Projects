from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get().capitalize()
    try:
        with open(file='data.json', mode='r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='Data file was not found.')
        window.focus()
        website_entry.focus()
    else:
        if website in data:
            password = data[website]['password']
            email = data[website]['email']
            messagebox.showinfo(title=website,
                                message=f'Email: {email}\nPassword: {password}\n\n'
                                        f'Password was copied into the clipboard')
            pyperclip.copy(password)
            window.focus()
            website_entry.focus()

        else:
            if website == '':
                messagebox.showerror(title='Not enough information!',
                                     message='You did not fill the required information.')

            else:
                messagebox.showerror(title='Error', message=f'Data regarding {website} does not exist in the data file.'
                                                            f'\nTry adding it first.')

            window.focus()
            website_entry.focus()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    chosen_letters = [choice(letters) for letter in range(randint(8, 10))]
    chosen_numbers = [choice(numbers) for num in range(randint(2, 4))]
    chosen_symbols = [choice(symbols) for sym in range(randint(2, 4))]

    password_list = chosen_letters + chosen_numbers + chosen_symbols
    shuffle(password_list)

    password = ''.join(password_list)
    password_entry.delete(0, END)
    pyperclip.copy(password)
    pop_up = Label(text='Password was copied into the clipboard', fg='red', pady=2, width=36,
                   font=('Arial', 17, 'bold'))
    pop_up.grid(row=5, column=1, columnspan=2)
    window.after(2500, lambda: pop_up.destroy())
    password_entry.insert(END, string=password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_entry.get().capitalize()
    info = user_entry.get().lower()
    user_password = password_entry.get()
    new_data = {
        website: {
            "email": info,
            "password": user_password,
        }
    }
    if website == '' or info == '' or user_password == '':
        messagebox.showerror(title='Not enough information!', message='You did not fill the required information')
        window.focus()
        website_entry.focus()
    else:
        try:
            with open(file='data.json', mode='r') as data:
                # We store the old data in 'file'.
                file = json.load(data)
        except FileNotFoundError:
            with open(file='data.json', mode='w') as data:
                json.dump(new_data, data, indent=4)
        else:
            # We update the old data with new data
            file.update(new_data)
            with open(file='data.json', mode='w') as data:
                # We write the data to a new json 'file'
                json.dump(file, data, indent=4)

                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Window settings.
window = Tk()
window.title('Password Manager')
window.configure(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
background_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=background_image)
canvas.grid(row=0, column=1)

# 'Website' label and entry.
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus_set()

# 'Email/Username' label and entry.
user_label = Label(text='Email/Username:')
user_label.grid(row=2, column=0)
user_entry = Entry(width=35)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(END, string='idan@gmail.com')

# 'Password' label and entry.
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
# 'Add' button.
add_button = Button(text='Add', width=36, command=add)
add_button.grid(row=4, column=1, columnspan=2)

# 'Generate password' button.
generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(row=3, column=2)

# 'Search' button.
search_button = Button(text='Search', width=13, command=find_password)
search_button.grid(column=2, row=1)


window.mainloop()
