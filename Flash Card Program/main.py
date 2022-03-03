from tkinter import *
import pandas
import random

# ------------------------------ CONSTANTS ------------------------------ #
BACKGROUND_COLOR = "#B1DDC6"
generated_word = {}
data = pandas.DataFrame()

# ------------------------------ Getting data ------------------------------ #
try:
    data = pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('./data/french_words.csv')
    with open('./data/words_to_learn.csv', 'w') as data_file:
        pass
    data.to_csv('./data/words_to_learn.csv', index=False)
finally:
    to_learn = data.to_dict(orient='records')


# ------------------------------ Button Functions ------------------------------ #
def flip_card():
    canvas.itemconfig(card_background, image=card_back)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=generated_word['English'], fill='white')


def next_card():
    global generated_word, flip_timer
    window.after_cancel(flip_timer)
    generated_word = random.choice(to_learn)
    canvas.itemconfig(card_background, image=card_front)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=generated_word['French'], fill='black')
    flip_timer = window.after(3000, flip_card)


def got_it_right():
    global generated_word, data
    to_learn.remove(generated_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv('./data/words_to_learn.csv')
    next_card()


# ------------------------------ SETTING UI ------------------------------ #
# Setting window.
window = Tk()
window.title('Flash Card Program')
window.configure(background=BACKGROUND_COLOR, pady=50, padx=50)

# Setting the flash card graphics.
card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'), fill='black')
card_word = canvas.create_text(400, 263, text='word', font=('Ariel', 60, 'bold'), fill='black')
canvas.grid(row=0, column=0, columnspan=2)

# Setting buttons
right_image = PhotoImage(file='./images/right.png')
right_button = Button(image=right_image, highlightthickness=0, command=got_it_right)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

# Setting a 3-second timer.
flip_timer = window.after(3000, flip_card)

next_card()

window.mainloop()

