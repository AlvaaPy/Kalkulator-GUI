from tkinter import *
from math import pow

# Initialize the main window
window = Tk()
window.title("Kalkulator GUI dengan Python")
window.geometry('400x400')
window.configure(bg='#f0f0f0')  # Set the background color

# Styling options
label_font = ("Helvetica", 12)
entry_font = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")
button_bg = "#4CAF50"  # Button background color
button_fg = "#FFFFFF"  # Button text color

# Create and place labels
lbl = Label(window, text="Masukan Nilai Pertama:", anchor="e", width=20, font=label_font, bg='#f0f0f0')
lbl.grid(column=0, row=0, padx=10, pady=10)

lbl2 = Label(window, text="Masukan Nilai Kedua:", anchor="e", width=20, font=label_font, bg='#f0f0f0')
lbl2.grid(column=0, row=1, padx=10, pady=10)

lbl3 = Label(window, text="Hasil:", anchor="e", width=20, font=label_font, bg='#f0f0f0')
lbl3.grid(column=0, row=2, padx=10, pady=10)

# Create and place entry fields
nilai1 = Entry(window, width=20, font=entry_font)
nilai1.grid(column=1, row=0, padx=10, pady=10)

nilai2 = Entry(window, width=20, font=entry_font)
nilai2.grid(column=1, row=1, padx=10, pady=10)

hasil = Label(window, text="0", anchor="w", width=20, font=label_font, bg='#f0f0f0')
hasil.grid(column=1, row=2, padx=10, pady=10)

# Define calculator functions
def tambah():
    hasil.configure(text=(float(nilai1.get()) + float(nilai2.get())))

def kurang():
    hasil.configure(text=(float(nilai1.get()) - float(nilai2.get())))

def kali():
    hasil.configure(text=(float(nilai1.get()) * float(nilai2.get())))

def bagi():
    hasil.configure(text=(float(nilai1.get()) / float(nilai2.get())))

def pangkat():
    hasil.configure(text=(pow(float(nilai1.get()), float(nilai2.get()))))

def akar():
    hasil.configure(text=(pow(float(nilai1.get()), 1 / float(nilai2.get()))))

def modulus():
    hasil.configure(text=(float(nilai1.get()) % float(nilai2.get())))

# Create and place buttons in a 3x3 grid
btnTambah = Button(window, text="Tambah", command=tambah, font=button_font, bg=button_bg, fg=button_fg)
btnTambah.grid(column=0, row=3, padx=10, pady=10)

btnKurang = Button(window, text="Kurang", command=kurang, font=button_font, bg=button_bg, fg=button_fg)
btnKurang.grid(column=1, row=3, padx=10, pady=10)

btnKali = Button(window, text="Kali", command=kali, font=button_font, bg=button_bg, fg=button_fg)
btnKali.grid(column=2, row=3, padx=10, pady=10)

btnBagi = Button(window, text="Bagi", command=bagi, font=button_font, bg=button_bg, fg=button_fg)
btnBagi.grid(column=0, row=4, padx=10, pady=10)

btnPangkat = Button(window, text="Pangkat", command=pangkat, font=button_font, bg=button_bg, fg=button_fg)
btnPangkat.grid(column=1, row=4, padx=10, pady=10)

btnAkar = Button(window, text="Akar", command=akar, font=button_font, bg=button_bg, fg=button_fg)
btnAkar.grid(column=2, row=4, padx=10, pady=10)

btnModulus = Button(window, text="Modulus", command=modulus, font=button_font, bg=button_bg, fg=button_fg)
btnModulus.grid(column=0, row=5, padx=10, pady=10)

# Run the main loop
window.mainloop()
