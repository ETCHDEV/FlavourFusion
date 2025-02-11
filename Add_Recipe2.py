from pathlib import Path
import tkinter as tk
from tkinter import Canvas, Entry, Text, Button, PhotoImage, messagebox
from controllers.recipe_controller import add_recipe

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame7")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = tk.Tk()
window.geometry("1096x700")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=700,
    width=1096,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
canvas.create_image(
    548.0,
    350.0,
    image=image_image_1
)

canvas.create_rectangle(
    0.0,
    0.0,
    1096.0,
    71.0,
    fill="#783000",
    outline="")

canvas.create_text(
    92.0,
    12.0,
    anchor="nw",
    text="Add Your Recipe",
    fill="#FFFFFF",
    font=("Inika Bold", 36 * -1)
)

fields = ["Recipe Name", "Ingredients", "Instructions", "Cuisine", "Category", "Video Link"]
entries = {}
y_position = 90

for field in fields:
    canvas.create_text(
        39.0,
        y_position,
        anchor="nw",
        text=field,
        fill="#FAFAFA",
        font=("Inika Bold", 24 * -1)
    )
    if field == "Instructions":
        entry = Text(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            height=4,
            width=60,
            highlightthickness=0,
            wrap="word",
            relief="flat"
        )
    else:
        entry = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            width=60,
            relief="flat"
        )
    entry.place(
        x=374.0,
        y=y_position,
        width=408.0,
        height=40.0
    )
    entries[field] = entry
    y_position += 50

def submit_recipe():
    data = {field: (entries[field].get("1.0", "end-1c") if field == "Instructions" else entries[field].get()) for field in fields}
    if not all(data.values()):
        messagebox.showerror("Error", "All fields are required!")
        return
    add_recipe(
        data["Recipe Name"],
        data["Category"],
        data["Ingredients"],
        data["Instructions"],
        data["Cuisine"],
        data["Video Link"]
    )
    messagebox.showinfo("Success", "Recipe added successfully!")

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=submit_recipe,
    relief="flat"
)
button_1.place(x=39.0, y=y_position - 20, width=224.0, height=71.0)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
canvas.create_image(38.0, 35.0, image=image_image_2)
window.resizable(False, False)
window.mainloop()
