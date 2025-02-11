from pathlib import Path
import tkinter as tk
from tkinter import Canvas, Entry, Button, PhotoImage, Listbox, Scrollbar, messagebox
from controllers.recipe_controller import search_recipes, get_recipe_by_id

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame4")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def perform_search():
    """Search recipes based on ingredients."""
    keyword = entry_1.get().strip()
    if not keyword:
        messagebox.showerror("Error", "Please enter ingredients to search.")
        return
    
    results = search_recipes(keyword, "ingredients")
    results_listbox.delete(0, tk.END)
    
    if results:
        for recipe in results:
            results_listbox.insert(tk.END, f"{recipe['recipe_id']} - {recipe['name']} ({recipe['cuisine']})")
    else:
        messagebox.showinfo("No Results", "No matching recipes found.")

def show_recipe_details(event):
    """Open a new window with full recipe details."""
    selected_index = results_listbox.curselection()
    if not selected_index:
        return
    
    selected_recipe = results_listbox.get(selected_index[0])
    recipe_id = selected_recipe.split(" - ")[0]
    
    try:
        recipe_id = int(recipe_id)
    except ValueError:
        messagebox.showerror("Error", "Invalid recipe selection.")
        return
    
    recipe = get_recipe_by_id(recipe_id)
    if not recipe:
        messagebox.showerror("Error", "Could not fetch recipe details.")
        return
    
    details_window = tk.Toplevel(window)
    details_window.title(f"Recipe: {recipe['name']}")
    
    for key, value in recipe.items():
        tk.Label(details_window, text=f"{key.capitalize()}: {value}", wraplength=400, justify="left").pack(anchor="w", padx=10, pady=2)

# GUI Setup
window = tk.Tk()
window.geometry("1095x660")
window.configure(bg="#FFFFFF")
canvas = Canvas(window, bg="#FFFFFF", height=660, width=1095, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
canvas.create_image(547.0, 330.0, image=image_image_1)
canvas.create_rectangle(0.0, 0.0, 1095.0, 62.0, fill="#7B5401", outline="")
canvas.create_text(76.0, 8.0, anchor="nw", text="Search Your Recipe", fill="#FFFFFF", font=("Inika", 36 * -1))
canvas.create_text(49.0, 85.0, anchor="nw", text="Enter your ingredients", fill="#010101", font=("Inika", 32 * -1))

# Search Entry Field
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
canvas.create_image(435.0, 156.5, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_1.place(x=32.0, y=136.0, width=806.0, height=39.0)

# Search Button
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=perform_search, relief="flat")
button_1.place(x=638.0, y=85.0, width=210.0, height=46.0)

canvas.create_text(49.0, 204.0, anchor="nw", text="Recipe Results", fill="#000000", font=("Inika", 32 * -1))

# Results Listbox with Scrollbar
frame = tk.Frame(window)
frame.place(x=49, y=250, width=900, height=300)
results_listbox = Listbox(frame, bg="white", fg="black", font=("Arial", 14))
results_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar = Scrollbar(frame, orient=tk.VERTICAL, command=results_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
results_listbox.config(yscrollcommand=scrollbar.set)
results_listbox.bind("<<ListboxSelect>>", show_recipe_details)

window.resizable(False, False)
window.mainloop()
