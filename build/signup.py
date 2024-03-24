


#backend 
from pathlib import Path
from subprocess import call
import sqlite3

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,messagebox


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"G:\TurfBookingSyS\build\assets\frame1")
conn=sqlite3.connect(r'build/user.db')
cursor=conn.cursor()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def validate_input_wallet(new_value):
    return new_value.isdigit() or new_value == ""

def validate_input_mobno(new_value):
    return (new_value.isdigit() and len(new_value) <= 10) or new_value == ""

def signup_user():
    # Get the text from the entries
    name = entry_3.get()
    email = entry_1_email.get()
    password = entry_2.get()
    wallet = entry_5.get()
    mobno = entry_4.get()

    # Check if any field is empty
    if not name or not email or not password or not wallet or not mobno:
        messagebox.showerror("Error", "All fields must be filled")
        return

    # Check if wallet entry is an integer
    if int(wallet) < 100:
        messagebox.showerror("Error", "Wallet entry should be at least 100")
        return

    with sqlite3.connect("build\\user.db") as db:
        cursor = db.cursor()
        # cursor.execute('DROP TABLE user')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                wallet INT NOT NULL,
                mobno TEXT NOT NULL
                
            );
        ''')
        cursor.execute("INSERT INTO user (name, email, password, wallet, mobno) VALUES (?, ?, ?, ?, ?)",
                       (name, email, password, int(wallet), mobno))
        
        db.commit()
        print("User created")
        window.destroy()  # Close the signup window
        call(["python", "build/login.py"])  # Open the login page


window = Tk()

window.geometry("827x463")
window.configure(bg = "#006AAE")


canvas = Canvas(
    window,
    bg = "#006AAE",
    height = 463,
    width = 827,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    283.0,
    0.0,
    827.0,
    463.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    318.0,
    77.0,
    anchor="nw",
    text="Create Account",
    fill="#303030",
    font=("Poppins SemiBold", 28 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    442.5,
    246.5,
    image=entry_image_1
)
entry_1_email = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Poppins SemiBold", 18 * -1)
)
entry_1_email.place(
    x=352.0,
    y=232.0,
    width=181.0,
    height=31.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    442.5,
    318.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=352.0,
    y=304.0,
    width=181.0,
    height=31.0
)

canvas.create_text(
    354.0,
    287.0,
    anchor="nw",
    text="password",
    fill="#000000",
    font=("Poppins SemiBold", 10 * -1)
)

canvas.create_text(
    354.0,
    215.0,
    anchor="nw",
    text="email",
    fill="#000000",
    font=("Poppins SemiBold", 10 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    442.5,
    181.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=352.0,
    y=167.0,
    width=181.0,
    height=31.0
)

canvas.create_text(
    354.0,
    150.0,
    anchor="nw",
    text="name",
    fill="#000000",
    font=("Poppins SemiBold", 10 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    694.5,
    181.5,
    image=entry_image_4
)
vcmd = window.register(validate_input_mobno)
entry_4 = Entry(window, validate="key", validatecommand=(vcmd, '%P'),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=604.0,
    y=167.0,
    width=181.0,
    height=31.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    694.5,
    246.5,
    image=entry_image_5
)
vcmd = window.register(validate_input_wallet)
entry_5 = Entry(window, validate="key", validatecommand=(vcmd, '%P'),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=604.0,
    y=230.0,
    width=181.0,
    height=31.0
)

canvas.create_text(
    609.0,
    215.0,
    anchor="nw",
    text="Wallet ",
    fill="#000000",
    font=("Poppins SemiBold", 10 * -1)
)

canvas.create_text(
    604.0,
    150.0,
    anchor="nw",
    text="Mob No.",
    fill="#000000",
    font=("Poppins SemiBold", 10 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    200.0,
    230.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    326.0,
    39.0,
    image=image_image_2
)

canvas.create_text(
    343.0,
    27.0,
    anchor="nw",
    text="EK-TURF-A",
    fill="#303030",
    font=("RedHatDisplay Bold", 18 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
     command=lambda: [print("button_1 clicked"), signup_user()][1],
    relief="flat",
    bg="#ffffff"
)
button_1.place(
    x=428.0,
    y=377.0,
    width=262.0,
    height=74.55769348144531
)

canvas.create_text(
    765.0,
    236.0,
    anchor="nw",
    text="Rs",
    fill="#000000",
    font=("Poppins SemiBold", 14 * -1)
)

window.resizable(False, False)
window.mainloop()
