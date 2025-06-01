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

# Text boxes
original_text = Text(window, height=10, width=40)
original_text.grid(column=0, row=0, pady=20, padx=10)

translate_button = Button(window, text="Translate!", font=("Helvetica", 24), command=translate)
translate_button.grid(row=0, column=1, padx=10)

translated_text = Text(window, height=10, width=40)
translated_text.grid(column=2, row=0, pady=20, padx=10)

window.mainloop()