from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# -------------------------------- UI SETTINGS ---------------------------------#
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# Canvas of image
front_card = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
canvas.create_image(400, 265, image=front_card)
canvas.create_text(400, 120, text="Language", font=("Arial", 40, "italic"))
canvas.create_text(400, 300, text="Word", font=("Arial", 60, "bold"))

# Buttons
w_button_img = PhotoImage(file="images/wrong.png")
unknown_b = Button(image=w_button_img, highlightthickness=0)
unknown_b.grid(row=1, column=0)

r_button_img = PhotoImage(file="images/right.png")
known_b = Button(image=r_button_img, highlightthickness=0)
known_b.grid(row=1, column=1)

window.mainloop()
