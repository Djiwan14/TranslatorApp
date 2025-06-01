from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox

# Window Setup
window = Tk()
window.title("Dji Project - Translator")
window.geometry("880x500")

icon_photo = PhotoImage(file='icon.png')
window.iconphoto(False, icon_photo)

# Functions
def translate():
    pass

def clear():
    """CLear text boxes"""
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)

# Text boxes
original_text = Text(window, height=10, width=40)
original_text.grid(column=0, row=0, pady=20, padx=10)

translated_text = Text(window, height=10, width=40)
translated_text.grid(column=2, row=0, pady=20, padx=10)

#Buttons

translate_button = Button(window, text="Translate!", font=("Helvetica", 24), command=translate)
translate_button.grid(row=0, column=1, padx=10)

clear_button = Button(window, text="Clear", command=clear)
clear_button.grid(row=2, column=1)

language_list = [1, 2, 3, 4, 4, 4 ,45, 4, 2, 2, 8, 9, 9, 4, 87, 6, 8, 1, 4, 4, 8, 4, 2]

# Combo boxes
original_combo = ttk.Combobox(window, width=50, value=language_list)
original_combo.current(21)
original_combo.grid(row=1, column=0)

translated_combo = ttk.Combobox(window, width=50, value=language_list)
translated_combo.current(22)
translated_combo.grid(row=1, column=2)

window.mainloop()