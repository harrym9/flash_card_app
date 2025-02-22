from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# -------------------------------- WORK WITH DATA ---------------------------------#
data = pandas.read_csv("data/english_words.csv")
words = data.to_dict(orient="records")


def next_word():
    current_word = random.choice(words)

    canvas.itemconfig(image, image=front_card)
    canvas.itemconfig(language_text, text="English")
    canvas.itemconfig(language_word, text=current_word["English"])

    def translate_word():
        canvas.itemconfig(image, image=back_card)
        canvas.itemconfig(language_text, text="Russian")
        canvas.itemconfig(language_word, text=current_word["Russian"])

    window.after(3000, func=translate_word)


# -------------------------------- UI SETTINGS ---------------------------------#
window = Tk()
window.title("Flashy")
window.config(pady=20, padx=20, bg=BACKGROUND_COLOR)

# Canvas of image
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
image = canvas.create_image(400, 265, image=front_card)
language_text = canvas.create_text(400, 120, text="", font=("Arial", 40, "italic"))
language_word = canvas.create_text(400, 300, text="", font=("Arial", 60, "bold"))

# Buttons
w_button_img = PhotoImage(file="images/wrong.png")
unknown_b = Button(image=w_button_img, highlightthickness=0, borderwidth=0, background=BACKGROUND_COLOR,
                   command=next_word)
unknown_b.grid(row=1, column=0)

r_button_img = PhotoImage(file="images/right.png")
known_b = Button(image=r_button_img, highlightthickness=0, borderwidth=0, background=BACKGROUND_COLOR,
                 command=next_word)
known_b.grid(row=1, column=1)

next_word()

window.mainloop()
