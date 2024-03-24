import sqlite3
from pathlib import Path
from subprocess import call
from datetime import datetime

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,messagebox
conn=sqlite3.connect(r'build/user.db')
cursor=conn.cursor()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"G:\TurfBookingSyS\build\assets\frame0")
#destroyss
def open_signup_page():
    window.withdraw()
    call(["python","build\signup.py"])
    window.deiconify()
    
def open_home_page():
    window.withdraw() 
    call(["python","build\homepage.py"])
    window.geometry("+100+400")
    


def validate_credentials():
    username_or_email = entry_1.get()
    password = entry_2.get()

    with sqlite3.connect(r"build\user.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM user WHERE (email = ? OR name = ?) AND password = ?", (username_or_email, username_or_email, password))
        user = cursor.fetchone()

    if user is None:
        messagebox.showerror("Error", "Invalid username/email or password")
        return False
    else:
        # Insert the user's details into the current_user table
        cursor.execute("INSERT INTO current_user (name, email, login_time) VALUES (?, ?, ?)", (user[1], user[2], datetime.now().isoformat()))
        
        # Update the 'wallet' column in the 'current_user' table with the corresponding values from the 'user' table
        cursor.execute("""
            UPDATE current_user 
            SET wallet = (
                SELECT wallet 
                FROM user 
                WHERE user.name = current_user.name
            )
        """)
        
        db.commit()
        return True
  

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
# cursor.execute('DROP TABLE current_user')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS current_user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        login_time TEXT NOT NULL,
        wallet INTEGER,
        FOREIGN KEY(name, email) REFERENCES user(name, email)
    );
''')
# Add a new column 'wallet' to the 'current_user' table
# cursor.execute("ALTER TABLE current_user ADD COLUMN wallet INTEGER")

# Update the 'wallet' column in the 'current_user' table with the corresponding values from the 'user' table
# cursor.execute("""
#     UPDATE current_user 
#     SET wallet = (
#         SELECT wallet 
#         FROM user 
#         WHERE user.name = current_user.name
#     )
# """)

conn.commit()


window = Tk()

window.geometry("827x463")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 463,
    width = 827,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    682.0,
    231.0,
    image=image_image_1
)

canvas.create_text(
    32.0,
    60.0,
    anchor="nw",
    text="Login",
    fill="#303030",
    font=("Poppins SemiBold", 32 * -1)
)

canvas.create_text(
    31.0,
    108.0,
    anchor="nw",
    text="Login to access your travelwise  account",
    fill="#303030",
    font=("Poppins Regular", 12 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    bg="#ffffff"
)
button_1.place(
    x=23.0,
    y=318.0,
    width=125.0,
    height=20.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat",
    bg="#ffffff"
)
button_2.place(
    x=161.0,
    y=320.0,
    width=101.0,
    height=18.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=open_signup_page,
    relief="flat",
    bg="#ffffff"
)
button_3.place(
    x=30.0,
    y=363.0,
    width=210.0,
    height=18.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    49.0,
    32.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    156.5,
    178.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=43.0,
    y=164.0,
    width=227.0,
    height=31.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    155.5,
    233.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=42.0,
    y=219.0,
    width=227.0,
    height=31.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    433.0,
    226.0,
    image=image_image_3
)
def on_login_button_clicked():
    if validate_credentials():
        open_home_page()
button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=on_login_button_clicked,
    relief="flat",
    bg="#ffffff"
)
button_4.place(
    x=35.0,
    y=266.0,
    width=242.0,
    height=52.0
)

canvas.create_text(
    66.0,
    20.0,
    anchor="nw",
    text="EK-TURF-A",
    fill="#303030",
    font=("RedHatDisplay Bold", 18 * -1)
)

canvas.create_text(
    45.0,
    147.0,
    anchor="nw",
    text="email/username",
    fill="#000000",
    font=("Poppins SemiBold", 11 * -1)
)

canvas.create_text(
    40.0,
    202.0,
    anchor="nw",
    text="password",
    fill="#000000",
    font=("Poppins SemiBold", 11 * -1)
)
window.resizable(False, False)
window.mainloop()
