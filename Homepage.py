
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
import subprocess
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from Login import open_login_page


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_file(pyfile):
    window.destroy()  # First close the current window
    subprocess.Popen(["python3", pyfile])

window = Tk()

window.geometry("1096x658")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 658,
    width = 1096,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    787.0,
    0.0,
    1096.0,
    658.0,
    fill="#58D373",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    1096.0,
    64.0,
    fill="#405936",
    outline="")

canvas.create_text(
    74.0,
    17.0,
    anchor="nw",
    text="Flavour fusion",
    fill="#FFFFFF",
    font=("Inika", 24 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    34.0,
    32.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    393.0,
    361.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    844.0,
    361.0,
    image=image_image_3
)

canvas.create_text(
    699.0,
    98.0,
    anchor="nw",
    text="Flavour fusion",
    fill="#841113",
    font=("Inika", 48 * -1)
)

#Register Button
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_file("Register.py"),
    relief="flat"
)
button_1.place(
    x=267.0,
    y=454.0,
    width=160.0,
    height=42.0
)

#Sign In Button
button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_login_page(window),
    relief="flat"
)
button_5.place(
    x=68.0,
    y=452.0,
    width=160.0,
    height=42.0
)
window.resizable(False, False)
window.mainloop()
