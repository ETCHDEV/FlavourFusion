import tkinter as tk
from tkinter import ttk, Canvas, Entry, Button, PhotoImage, messagebox
import sqlite3
from pathlib import Path

# Database function to fetch data
def fetch_data():
    try:
        with sqlite3.connect("your_database.db") as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA table_info(your_table)")
            columns = [col[1] for col in cursor.fetchall()]

            tree["columns"] = columns
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=120)

            cursor.execute("SELECT * FROM your_table")
            rows = cursor.fetchall()

            tree.delete(*tree.get_children())
            for row in rows:
                tree.insert('', 'end', values=row)
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Error fetching data: {e}")

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame6")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = tk.Tk()
window.geometry("1095x661")
window.configure(bg="#BE9494")

canvas = Canvas(
    window,
    bg="#BE9494",
    height=661,
    width=1095,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)
canvas.create_text(
    42.0,
    90.0,
    anchor="nw",
    text="Username",
    fill="#000000",
    font=("Inika Bold", 24 * -1)
)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_1.place(x=201.0, y=85.0, width=251.0, height=39.0)

canvas.create_text(42.0, 162.0, anchor="nw", text="Email", fill="#000000", font=("Inika Bold", 24 * -1))
entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_2 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_2.place(x=201.0, y=157.0, width=251.0, height=39.0)

canvas.create_text(42.0, 234.0, anchor="nw", text="Password", fill="#000000", font=("Inika Bold", 24 * -1))
entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_3 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_3.place(x=201.0, y=229.0, width=251.0, height=39.0)

canvas.create_text(524.0, 90.0, anchor="nw", text="Phone No", fill="#000000", font=("Inika Bold", 24 * -1))
entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_4 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_4.place(x=675.0, y=85.0, width=251.0, height=39.0)

canvas.create_rectangle(0.0, 0.0, 1095.0, 61.0, fill="#471212", outline="")
canvas.create_text(83.0, 7.0, anchor="nw", text="Manage Profile", fill="#FFFFFF", font=("Inika Bold", 36 * -1))

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: print("button_1 clicked"), relief="flat")
button_1.place(x=516.0, y=226.0, width=172.0, height=44.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=lambda: print("button_2 clicked"), relief="flat")
button_2.place(x=764.0, y=225.0, width=172.0, height=44.0)

# Frame to hold the SQLite Table
table_frame = tk.Frame(window)
table_frame.place(x=25, y=355, width=1045, height=267)

# Create the Treeview widget
tree = ttk.Treeview(table_frame, selectmode="browse")
vsb = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
vsb.pack(side="right", fill="y")
tree.configure(yscrollcommand=vsb.set)

hsb = ttk.Scrollbar(table_frame, orient="horizontal", command=tree.xview)
hsb.pack(side="bottom", fill="x")
tree.configure(xscrollcommand=hsb.set)

tree.pack(fill="both", expand=True)

# Refresh button
refresh_button = tk.Button(window, text="Refresh Data", command=fetch_data)
refresh_button.place(x=500, y=630)

fetch_data()
window.resizable(False, False)
window.mainloop()
