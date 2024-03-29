


from pathlib import Path
from subprocess import call

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"G:\TurfBookingSyS\build\assets\frame2")

def open_grp_booking():
    window.withdraw()
    call(["python","build\groupbook.py"])
    window.geometry("+100+400")
    window.deiconify()

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
    x=38.0,
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
    x=41.0,
    y=309.0,
    width=192.0,
    height=35.0
)

canvas.create_text(
    302.0,
    332.0,
    anchor="nw",
    text="Featured Listing",
    fill="#398564",
    font=("Poppins SemiBold", 30 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat",
    bg="#ffffff"
)
button_3.place(
    x=1224.0,
    y=344.0,
    width=96.0,
    height=35.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1200.0,
    361.6500244140625,
    image=image_image_2
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
    x=27.0,
    y=379.0,
    width=192.0,
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
    x=44.0,
    y=454.0,
    width=216.0,
    height=35.0
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
    x=59.0,
    y=530.0,
    width=177.0,
    height=70.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=open_grp_booking,
    relief="flat",
    bg="#000000"
)
button_7.place(
    x=52.0,
    y=623.0,
    width=226.0,
    height=35.0
)

canvas.create_text(
    58.0,
    102.0,
    anchor="nw",
    text="EK-TURF-A",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 30 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    139.0,
    65.99999182952581,
    image=image_image_3
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat",
    bg="#FFFFFf"
)
button_8.place(
    x=302.0,
    y=393.0,
    width=321.0,
    height=322.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat",
    bg="#ffffff"
)
button_9.place(
    x=643.0,
    y=393.0,
    width=321.0,
    height=322.0
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    803.0,
    156.0,
    image=image_image_4
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat",
    bg="#ffffff"
)
button_10.place(
    x=984.0,
    y=392.0,
    width=327.0,
    height=323.0
)
window.resizable(False, False)
window.mainloop()
