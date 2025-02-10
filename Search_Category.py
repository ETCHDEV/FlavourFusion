from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
from controllers.recipe_controller import get_categories, search_by_category, get_recipe_by_id

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/arjun/FlavourFusion-GUI/build/assets/frame5")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = tk.Tk()
window.geometry("1095x660")
window.configure(bg="#FFFFFF")

canvas = tk.Canvas(
    window,
    bg="#FFFFFF",
    height=660,
    width=1095,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    547.0,
    330.0,
    image=image_image_1
)

canvas.create_rectangle(
    0.0,
    0.0,
    1095.0,
    60.0,
    fill="#3B1212",
    outline=""
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))  # Ensure the file exists in the assets folder
image_3 = canvas.create_image(
    15.0,
    7.0,
    image=image_image_3,
    anchor="nw"
)

canvas.create_text(
    83.0,
    7.0,
    anchor="nw",
    text="Categorize Your Recipe",
    fill="#FFFFFF",
    font=("Inika", 36 * -1)
)

canvas.create_text(
    48.0,
    97.0,
    anchor="nw",
    text="Select the Category ",
    fill="#000000",
    font=("Inika", 32 * -1)
)

def update_table(*args):
    selected_category = category_var.get()
    recipes = search_by_category(selected_category)
    table.delete(*table.get_children())
    for recipe in recipes:
        table.insert("", "end", values=(recipe["recipe_id"], recipe["name"]))

def show_recipe_details(event):
    selected_item = table.selection()
    if not selected_item:
        return
    recipe_id = table.item(selected_item, "values")[0]
    recipe = get_recipe_by_id(recipe_id)
    
    details_window = tk.Toplevel(window)
    details_window.title(f"Recipe: {recipe['name']}")
    for key, value in recipe.items():
        tk.Label(details_window, text=f"{key.capitalize()}: {value}", wraplength=400, justify="left").pack(anchor="w", padx=10, pady=2)

category_var = tk.StringVar()
categories = get_categories()
category_dropdown = ttk.Combobox(window, textvariable=category_var, values=categories, state="readonly")
category_dropdown.place(x=50, y=140, width=300, height=40)
category_var.trace_add("write", update_table)

canvas.create_text(
    48.0,
    202.0,
    anchor="nw",
    text="Results",
    fill="#000000",
    font=("Inika", 32 * -1)
)

table = ttk.Treeview(window, columns=("ID", "Name"), show="headings")
table.heading("ID", text="ID")
table.heading("Name", text="Name")
table.place(x=50, y=250, width=800, height=300)
table.bind("<Double-1>", show_recipe_details)

window.resizable(False, False)
window.mainloop()
