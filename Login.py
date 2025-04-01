import subprocess
import mysql.connector
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from tkinter import messagebox
from pathlib import Path

from Home_Login import open_hlogin_page

# Set up asset path handling
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame0")

# This function helps with relative path handling for assets like images
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_login_page(previous_window):
    previous_window.destroy()
    # Function to connect to the database
    def connect_db():
        return mysql.connector.connect(
            host="localhost",  # Adjust this as needed
            user="root",       # Your database username
            password="12345678",       # Your database password
            database="FlavourFusion"  # Name of your database
        )

    # Function to handle login
    def login_user():
        email = entry_1.get().strip()
        password = entry_2.get().strip()

        # Check if the email and password fields are empty
        if not email:
            messagebox.showerror("Input Error", "Email is required!")
            return
        if not password:
            messagebox.showerror("Input Error", "Password is required!")
            return

        # Connect to the database and check if the user exists
        db = connect_db()
        cursor = db.cursor()

        try:
            # Query to check if the email and password match in the database
            cursor.execute("SELECT * FROM users WHERE email = %s AND password_hash = %s", (email, password))
            user = cursor.fetchone()
            if user:
                if user[5] == 'YES':
                    open_file("Admin.py")  # Open the AdminPage after successful login  
                else:
                    open_hlogin_page(window, user[0])         
            else:
                messagebox.showerror("Invalid Credentials", "Incorrect email or password!")
                return
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"An error occurred: {err}")
            return
        finally:
            cursor.close()
            db.close()

    # Function to open a file (e.g., another Python script)
    def open_file(pyfile):
        window.destroy()  # First close the current window
        subprocess.Popen(["python3", pyfile])


    # Setup tkinter window for login
    window = Tk()
    window.geometry("915x610")
    window.configure(bg="#FFFFFF")

    # Create the canvas
    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=610,
        width=915,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    # Background image
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(457.0, 305.0, image=image_image_1)

    # Email label and input field
    canvas.create_text(
        493.0,
        320.0,
        anchor="nw",
        text="Email",
        fill="#000000",
        font=("Inika", 36 * -1)
    )

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(749.5, 336.0, image=entry_image_1)
    entry_1 = Entry(
        bd=0,
        bg="#B3AFAF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(x=664.0, y=320.0, width=171.0, height=30.0)

    # Password label and input field
    canvas.create_text(
        474.0,
        386.0,
        anchor="nw",
        text="Password",
        fill="#000000",
        font=("Inika", 32 * -1)
    )

    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(749.5, 410.5, image=entry_image_2)
    entry_2 = Entry(
        bd=0,
        bg="#B4AFAF",
        fg="#000716",
        highlightthickness=0,
        show="*"  # Mask the password input
    )
    entry_2.place(x=664.0, y=393.0, width=171.0, height=33.0)

    # Sign In button
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=login_user,  # Call login_user() when the button is clicked
        relief="flat"
    )
    button_1.place(x=684.0, y=469.0, width=131.0, height=44.0)

    canvas.create_text(
        443.0,
        153.0,
        anchor="nw",
        text="Login",
        fill="#FFFFFF",
        font=("Inika Bold", 40 * -1)
    )

    # Disable resizing
    window.resizable(False, False)

    # Run the main loop
    window.mainloop()


