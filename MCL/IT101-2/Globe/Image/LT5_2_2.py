from tkinter import *
from PIL import ImageTk, Image
import os

master = Tk()
master.title('Your Name Please')
master.geometry('500x200')
master.columnconfigure(0, weight=1)
master.columnconfigure(1, weight=1)

# Frames
frameOne = Frame(master)
frameOne.pack(side='top')
frameTwo = Frame(master)
frameTwo.pack(side='left', anchor='w', padx=20)
frameThree = Frame(master)
frameThree.pack(side='left')

# Inserts countries into listbox
def Countries():
    countries = continents[v.get()]
    n = 0
    countList.delete(0, END)
    for i in countries:
        countList.insert(n, i)
        n += 1

# Displays country flag
def picture(countList):
    country = countList.widget
    for i in country.curselection():
        val = country.get(i)
    folder_path = "Globe"
    png = os.path.join(folder_path, val + '.png')
    n = Image.open(png)  # opens image file
    n = n.resize((250, 130), Image.LANCZOS)  # resizes image to fit 500x200 geometry
    img = ImageTk.PhotoImage(n)
    lbl_img = Label(frameThree, image=img)
    lbl_img.image = img
    lbl_img.grid(row=0, column=0)

v = StringVar()

continents = {
    "Asia": ["Philippines", "Malaysia", "Taiwan", "Singapore", "Thailand", "India"],
    "Africa": ["Algeria", "Angola", "Egypt", "Cape Verde", "Liberia", "Kenya", "Morocco", "Nigeria"],
    "America": ["Venezuela", "Peru", "Jamaica", "United States", "Cuba", "Chile", "Argentina"],
    "Europe": ["Russia", "Germany", "United Kingdom", "Italy", "Ukraine", "France", "Belgium"]
}

# Radio buttons created using dictionary continents
n = 0
for (text, value) in continents.items():
    radio = Radiobutton(frameOne, text=text, variable=v,
                        value=text, bg='white', fg='blue', relief=RIDGE, font='times 14 bold', width=8,
                        command=lambda: Countries())
    radio.grid(row=0, column=n, pady=5)
    n += 1

# Scrollbar for listbox
scrollbar = Scrollbar(frameTwo)
scrollbar.pack(side='right', fill=Y)

# Country listbox
countList = Listbox(frameTwo, height=5, width=12, yscrollcommand=scrollbar.set, font='times 12')
countList.pack()
scrollbar.config(command=countList.yview)

# Calls def picture() every time a country is selected
countList.bind('<<ListboxSelect>>', picture)

master.mainloop()
