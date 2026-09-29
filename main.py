from tkinter import *
import random
import pandas


BACKGROUND_COLOR = "#B1DDC6"
WORD = {}


# --------------------------------------- LEARNED OR NOT ------------------------------------------

def memorized_word():
    global WORD, to_learn
    
    to_learn.remove(WORD)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/data_file_practice.csv", index = False)
    canvas.itemconfig(img_front, image = front_image)
    
    new_card()
    
    
def to_be_memorized():
    global WORD, to_learn
    
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/data_file_practice.csv", index = False)
    canvas.itemconfig(img_front, image = front_image)
    
    new_card()
    


# -------------------------------------- FLASH CARD SETUP -----------------------------------------

def flip_card():
    canvas.itemconfig(img_front, image = back_image)
    canvas.itemconfig(title, text = "English")
    canvas.itemconfig(word, text = f"{WORD['English']}")
    
    
    
    
# -------------------------------------- CHANGE FLASH CARD ----------------------------------------
to_learn = {}
try:
    data = pandas.read_csv("./data/data_file_practice.csv")
    
    
except FileNotFoundError:
    orignal_data = pandas.read_csv("./data/pashto_words.csv")
    to_learn = orignal_data.to_dict(orient = "records")
    
else:
    to_learn = data.to_dict(orient = "records")
    

def new_card():
    global WORD, flip_timer, to_learn
    window.after_cancel(flip_timer)
    
    WORD.update(random.choice(to_learn))
    canvas.itemconfig(title, text = "Pashto")
    canvas.itemconfig(word, text = f"{WORD['Pashto']}")
    
    flip_timer = window.after(3000, flip_card)


# ------------------------------------------- UI SETUP --------------------------------------------

window = Tk()
window.title("Flash Card App")
window.config(padx = 50, pady = 50, background = BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

front_image = PhotoImage(file = "images/card_front.png")
back_image = PhotoImage(file = "images/card_back.png")
right_image = PhotoImage(file = "images/right.png")
wrong_image = PhotoImage(file = "images/wrong.png")

canvas = Canvas(width = 800, height= 526)
img_front = canvas.create_image(400, 263, image = front_image)
canvas.config(background = BACKGROUND_COLOR, highlightthickness = 0)


title = canvas.create_text(400, 160, text = "Word", font = ("Arial", 60, "bold"))
word = canvas.create_text( 400, 290, text = "Meaning", font = ("Arial", 55, "italic"))
canvas.grid(column = 0, row = 0, columnspan = 3)


right_button = Button(image = right_image, command = memorized_word)
right_button.grid(column = 0, row = 1)


wrong_button = Button(image = wrong_image, command = to_be_memorized)
wrong_button.grid(column = 2, row = 1)





new_card()





window.mainloop()