from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
vi = '✔'
timer = None
hours = 0
# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    head_line.config(text='Timer', fg=GREEN)
    check_marks.config(text='')
    canvas.itemconfig(timer_text, text='00:00')
    global reps
    reps = 0
    global hours
    hours = 0
    hours_label.config(text=hours)
    window.after_cancel(timer)
    start_button['state'] = 'normal'

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    start_button['state'] = 'disabled'
    global reps
    global hours
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        head_line.config(text='Long Break', fg=RED)
        check_marks.config(text='')
        reps = 0
        hours += 1
        hours_label.config(text=hours)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        head_line.config(text='Short Break', fg=PINK)
        countdown(short_break_sec)
    else:
        head_line.config(text='Working Time', fg=GREEN)
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    global reps
    minutes = math.floor(count / 60)
    seconds = math.floor(count % 60)
    if int(minutes) < 10:
        minutes = f'0{minutes}'
        if int(seconds) < 10:
            seconds = f'0{seconds}'
    if int(seconds) == 0:
        seconds = '00'
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        if reps % 2 != 0:
            total_marks = vi * math.ceil((reps/2))
            check_marks.config(text=total_marks)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #


# Setting up the background.
window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro")

# Setting up the background image and clock text.
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
background_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=background_image)
timer_text = canvas.create_text(103, 130, text="00:00", font=(FONT_NAME, 35, 'bold'), fill='white')
canvas.grid(row=1, column=1)

# Setting the big timer above the tomato.
head_line = Label(text='TIMER', font=(FONT_NAME, 50, 'bold'), bg=YELLOW, fg=GREEN)
head_line.grid(row=0, column=1)

# Setting 'start' button.
start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

# Setting 'Reset' button.
reset_button = Button(text='Reset', highlightthickness=0, command=reset)
reset_button.grid(row=2, column=2)

# Setting the check marks after 25 minutes of work.
check_marks = Label(text='', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, 'bold'))
check_marks.grid(row=2, column=1)
check_marks.configure(pady=20)

# Setting label for total hours of work.
total_hours_label = Label(text='Total hours', font=(FONT_NAME, 20, 'bold'), fg='black', bg=YELLOW)
total_hours_label.grid(column=1, row=3)
total_hours_label.configure(pady=20)
hours_label = Label(text=hours, font=(FONT_NAME, 20, 'bold'), fg='black', bg=YELLOW)
hours_label.grid(column=1, row=4)
window.mainloop()

