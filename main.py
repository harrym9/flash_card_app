from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# -------------------------------- WORK WITH DATA ---------------------------------#
data = pandas.read_csv("data/english_words.csv")
words = data.to_dict(orient="records")


def next_word():
    global current_card, flipping_time
    window.after_cancel(flipping_time)

    current_card = random.choice(words)
    canvas.itemconfig(image, image=card_front)
    canvas.itemconfig(card_language, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")
    window.after(3000, func=translate_word)


def translate_word():
    canvas.itemconfig(image, image=card_back)
    canvas.itemconfig(card_language, text="Russian", fill="white")
    canvas.itemconfig(card_word, text=current_card["Russian"], fill="white")


# -------------------------------- UI SETTINGS ---------------------------------#
window = Tk()
window.title("Flashy")
window.config(pady=20, padx=20, bg=BACKGROUND_COLOR)
flipping_time = window.after(3000, func=translate_word)

# Canvas of image
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
image = canvas.create_image(400, 265, image=card_front)

card_language = canvas.create_text(400, 120, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 300, text="", font=("Arial", 60, "bold"))

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
