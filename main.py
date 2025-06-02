from tkinter import *
import googletrans
from tkinter import ttk, messagebox
from googletrans import Translator
import os
import sys


# Window Setup
window = Tk()
window.title("Dji Project - Translator")
window.geometry("880x500")

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

icon_photo = PhotoImage(file=resource_path("icon.png"))
window.iconphoto(False, icon_photo)

# Functions
def translate_it():
    """ We get the value of the language from the dropdown and with the help of that we get the key from languages
    dictionary. """
    # Clean All Previous Texts
    translated_text.delete(1.0, END)
    try:
        # Get Languages From Dictionary Keys
        from_language_key = [key for key, value in languages.items() if value == original_combo.get()][0]
        to_language_key = [key for key, value in languages.items() if value == translated_combo.get()][0]

        # In order to interact with textbox field, we have to specify the boundaries that words should be in
        # Turn original text to the TextBlob
        original_words = original_text.get(1.0, END)

        # Translate text
        translator = Translator()
        translated = translator.translate(original_words, src=from_language_key, dest=to_language_key)

        # Output the translated text to the screen
        translated_text.insert(1.0, translated.text)

    except Exception as e:
        messagebox.showerror("Tranlator", e)

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
translate_button = Button(window, text="Translate!", font=("Helvetica", 24), command=translate_it)
translate_button.grid(row=0, column=1, padx=10)

clear_button = Button(window, text="Clear", command=clear)
clear_button.grid(row=2, column=1)

# Grab the Language List from GoogleTrans
languages = googletrans.LANGUAGES

# Convert the dictionary to the list
language_list = list(languages.values())

# Combo boxes
original_combo = ttk.Combobox(window, width=50, value=language_list)
original_combo.current(21)
original_combo.grid(row=1, column=0)

translated_combo = ttk.Combobox(window, width=50, value=language_list)
translated_combo.current(30)
translated_combo.grid(row=1, column=2)

window.mainloop()