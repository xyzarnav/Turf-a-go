



from pathlib import Path
import sqlite3
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"G:\TurfBookingSyS\build\assets\frame5")
conn=sqlite3.connect(r'build/user.db')
cursor=conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts(
        name TEXT NOT NULL,
        number INTEGER NOT NULL,
        wallet_balance REAL NOT NULL,
        total_spending REAL NOT NULL,
        add_money REAL NOT NULL,
        FOREIGN KEY(name) REFERENCES user(name)
    )
''')
conn.commit()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS session(
        user_id INTEGER
    )
''')
# Commit the changes and close the connection

def login(user_id):
    cursor.execute("DELETE FROM session")  # Clear the previous session
    cursor.execute("INSERT INTO session VALUES (?)", (user_id,))  # Store the new user_id
    conn.commit()

# Function to get the ID of the currently logged-in user
def get_logged_in_user_id():
    cursor.execute("SELECT user_id FROM session")
    user_id = cursor.fetchone()
    return user_id[0] if user_id else None
current_user_id = get_logged_in_user_id()
try:
    # Fetch the name of the currently logged-in user
    cursor.execute("SELECT name FROM user WHERE name = ?", (current_user_id,))
    current_user_name = cursor.fetchone()[0]
except TypeError:
    current_user_name = "User not found"
    
try:
    # Fetch the mobile number of the currently logged-in user
    cursor.execute("SELECT mobno FROM user WHERE name = ?", (current_user_name,))
    current_user_mobile_number = cursor.fetchone()[0]
except TypeError:
    current_user_mobile_number = "Mobile number not found"
    #_______________________________________________________________________!_______________!______!_!_!_!____
try:
    # Fetch the latest name from the user table
    cursor.execute("SELECT name FROM user ORDER BY id DESC LIMIT 1")
    latest_user_name = cursor.fetchone()[0]
except TypeError:
    latest_user_name = "User not found"

try:
    # Fetch the latest mobile number from the user table
    cursor.execute("SELECT mobno FROM user ORDER BY id DESC LIMIT 1")
    latest_user_mobile_number = cursor.fetchone()[0]
except TypeError:
    latest_user_mobile_number = "Mobile number not found"


try:
    # Fetch the latest wallet balance from the user table
    cursor.execute("SELECT wallet FROM user ORDER BY id DESC LIMIT 1")
    latest_user_wallet_balance = cursor.fetchone()[0]
except TypeError:
    latest_user_wallet_balance = "Wallet balance not found"

#_______________________________________________________--@


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1340x740")
window.configure(bg = "#000000")


canvas = Canvas(
    window,
    bg = "#000000",
    height = 740,
    width = 1340,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    802.6805419921875,
    369.4444580078125,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    bg="#000000"
)
button_1.place(
    x=48.0,
    y=239.0,
    width=163.0,
    height=35.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat",
    bg="#000000"
)
button_2.place(
    x=45.0,
    y=309.0,
    width=192.0,
    height=35.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat",
    bg="#000000"
)
button_3.place(
    x=45.0,
    y=379.0,
    width=192.0,
    height=35.0
)

canvas.create_text(
    495.0,
    56.0,
    anchor="nw",
    text="ACCOUNT",
    fill="#000000",
    font=("Poppins SemiBold", 50 * -1)
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat",
    bg="#000000"
)
button_4.place(
    x=45.0,
    y=454.0,
    width=216.0,
    height=35.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat",
    bg="#000000"
)
button_5.place(
    x=45.0,
    y=530.0,
    width=177.0,
    height=70.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat",
    bg="#000000"
)
button_6.place(
    x=48.0,
    y=623.0,
    width=226.0,
    height=35.0
)

canvas.create_text(
    58.0,
    102.0,
    anchor="nw",
    text="TURF-A-GO",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 30 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    139.0,
    65.99999182952581,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    1112.0,
    370.0,
    image=image_image_3
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    497.0,
    174.32486534118652,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=338.0507621765137,
    y=146.3451690673828,
    width=317.89847564697266,
    height=55.95939254760742
)

canvas.create_text(
    331.0,
    119.0,
    anchor="nw",
    text="Name",
    fill="#000000",
    font=("Poppins SemiBold", 17 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    443.0,
    397.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=339.0507621765137,
    y=369.0,
    width=207.89847564697266,
    height=56.0
)

canvas.create_text(
    331.0,
    338.0,
    anchor="nw",
    text="Wallet Balance",
    fill="#000000",
    font=("Poppins SemiBold", 17 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    728.5,
    397.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=624.0507621765137,
    y=369.0,
    width=208.89847564697266,
    height=56.0
)

canvas.create_text(
    610.0,
    338.0,
    anchor="nw",
    text="Total Spending ",
    fill="#000000",
    font=("Poppins SemiBold", 17 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    498.0,
    507.9796962738037,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=339.0507621765137,
    y=480.0,
    width=317.89847564697266,
    height=55.95939254760742
)

canvas.create_text(
    342.5634460449219,
    454.0,
    anchor="nw",
    text="Add Money",
    fill="#000000",
    font=("Poppins SemiBold", 17 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    495.0,
    270.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=336.0507621765137,
    y=242.0,
    width=317.89847564697266,
    height=56.0
)

canvas.create_text(
    329.0,
    215.0,
    anchor="nw",
    text="Mob-no",
    fill="#000000",
    font=("Poppins SemiBold", 17 * -1)
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=474.0,
    y=601.0,
    width=204.0,
    height=57.0
)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
entry_2.insert(0, latest_user_wallet_balance)
entry_5.insert(0, latest_user_mobile_number)
entry_1.insert(0, latest_user_name)
#_____________________________________________@

window.resizable(False, False)
window.mainloop()
