from tkinter import *


def convert_mile_to_km():
    entry_input = miles_entry.get()
    result = float(entry_input) * 1.609344
    f = '{0:.3g}'.format(result)
    km.config(text=f)


# Configuring the window
window = Tk()
window.title("Mile to KM Converter")
window.wm_minsize(width=400, height=100)

# Creating a place to enter the miles
miles_label = Label(text='Miles', width=5, font=('Ariel', 10, 'bold'))
miles_label.grid(column=3, row=0)
miles_entry = Entry(width=8)
miles_entry.grid(column=2, row=0)

# Creating the kilometers place to be shown after pressing calculate:
buffer_text = Label(text="is equal to ", font=('Ariel', 10, 'bold'))
buffer_text.grid(column=1, row=1)
buffer_text.config(padx=50)

km = Label(text='0', width=10, font=('Ariel', 10, 'bold'))
km.grid(column=2, row=1)

km_label = Label(text='KM', height=1, font=('Ariel', 10, 'bold'))
km_label.grid(column=3, row=1)

# Creating the convert button.
convert = Button(text='Convert', command=convert_mile_to_km)
convert.grid(row=2, column=2)


window.mainloop()