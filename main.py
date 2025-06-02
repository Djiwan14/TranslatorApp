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
    """ We get the value of the language from the dropdown and with the help of that we get the key from languages
    dictionary. """
    # Clean All Previous Texts
    translator.delete(1.0, END)
    try:
        # Get Languages From Dictionary Keys
        for key, value in languages.items():
            if value == original_combo.get():
                from_language_key = key

        for key, value in languages.items():
            if value == translated_combo.get():
                to_language_key = key

        # In order to interact with textbox field, we have to specify the boundaries that words should be in
        # Turn original text to the TextBlob
        words = textblob.Textblob(original_text.get(1.0, END))

        # Translate text
        words = words.translate(from_lang=from_language_key, to_lang=to_language_key)

        # Output the translated text to the screen
        translated_text.insert(1.0, words)

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

translate_button = Button(window, text="Translate!", font=("Helvetica", 24), command=translate)
translate_button.grid(row=0, column=1, padx=10)

clear_button = Button(window, text="Clear", command=clear)
clear_button.grid(row=2, column=1)

# Grab the Language List from GoogleTrans
languages = googletrans.LANGUAGES

# Convert the dictionary to the list
language_list = list(languages.values())

# Combo boxes
original_combo = ttk.Combobox(window, width=50, value=language_list)
original_combo.current(57)
original_combo.grid(row=1, column=0)

translated_combo = ttk.Combobox(window, width=50, value=language_list)
translated_combo.current(72)
translated_combo.grid(row=1, column=2)

window.mainloop()