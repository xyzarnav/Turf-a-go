
from pathlib import Path
from subprocess import call
from tkcalendar import DateEntry
from datetime import datetime, timedelta
import sqlite3
import random
from tkinter import messagebox
conn=sqlite3.connect(r'build/user.db')
cursor=conn.cursor()
from tkinter import Tk, Canvas, Entry, Text, Button,Checkbutton,PhotoImage,Toplevel,StringVar, Scrollbar, Frame,Canvas
#_________________#_____________________-#______________________#
def update_var_list(var_list, var, slot):
    if var.get() == "yes":  # If the checkbox is checked
        var_list.append((var, slot))  # Add the (var, slot) tuple to var_list
    else:
        var_list.remove((var, slot))
     
def calculate_payable(var_list):
    selected_slots = [slot for var, slot in var_list if var.get() == "yes"]
    return len(selected_slots)*500          #*price

def submit_time_slots(var_list):
    selected_slots = [slot for var, slot in var_list if var.get() == "yes"]
    return ' & '.join(selected_slots)  # return the selected slots as a string
    
def create_time_slots(start_time, end_time, interval):
    time_slots = []
    current_time = start_time
    while current_time < end_time:
        next_time = current_time + timedelta(hours=interval)
        time_slots.append(f"{current_time.strftime('%I:%M %p')} - {next_time.strftime('%I:%M %p')}")
        current_time = next_time
    return time_slots

def create_checkboxes(time_slots, window, time_entry):
    var_list = []
    for slot in time_slots:
        var = StringVar(value="no")
        
        def update_var(var, slot):
            var.set("yes" if var.get() == "no" else "no")
            

        checkbox = Checkbutton(window, text=slot, variable=var, onvalue="yes", offvalue="no", width=30, height=2, anchor='w', justify='center', relief='solid', bd=1, 
                               command=lambda slot=slot, var=var: update_var(var, slot))
        checkbox.pack(fill='both')
        
        var_list.append((var, slot))
    return var_list



def open_time_slots_window(time_entry,payable_entry):
    def submit_button_command():
       
        selected_slots_text = submit_time_slots(var_list)
        time_entry.insert(0, selected_slots_text)
        payable_amount = calculate_payable(var_list)  # pass the price per slot here
        payable_entry.delete(0, 'end')
        group_booking_checkbox = Checkbutton(checkbutton_frame,font='purple', text="Group Booking", variable=group_booking_var)
        payable_entry.insert(0, str(payable_amount))  # convert payable_amount to string before inserting
        print(f"Number of selected checkboxes: {payable_amount}")  # print the count to the terminal
        window.destroy()
    

   
#@@@@@@@@@@@@@@@@@@@@@@@@@@#
    def update_group_booking_var():
        global group_booking_var
        group_booking_var.set("no" if group_booking_var.get() == "yes" else "no")

#2@@@@@@@@@@@@@@@@@@@@@@@#
       
    window = Tk()
    window.geometry("250x500")
    entry_2 = Entry(window)
    entry_2.pack()

    # Create a Frame for the Scrollbar
    frame = Frame(window)
    frame.pack(fill='both', expand=True)

    # Create a Scrollbar
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")


    # Create a Canvas
    canvas = Canvas(frame, yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)

    # Configure the Scrollbar
    scrollbar.config(command=canvas.yview)
    
    # Create another Frame for the Checkbuttons
    checkbutton_frame = Frame(canvas)
    canvas.create_window((0, 0), window=checkbutton_frame, anchor="nw")
     # Create a checkbox for group booking

    group_booking_var = StringVar()
    group_booking_checkbox = Checkbutton(checkbutton_frame,font='purple', text="Group Booking", variable=group_booking_var, onvalue="yes", command=update_group_booking_var)
    start_time = datetime.strptime("6:00 AM", "%I:%M %p")
    end_time = datetime.strptime("11:00 PM", "%I:%M %p")
    time_slots = create_time_slots(start_time, end_time, 1) 
    var_list = create_checkboxes(time_slots, checkbutton_frame, time_entry)
    
    submit_button = Button(checkbutton_frame, text="Submit", command=submit_button_command, width=20, font='purple')
    submit_button.pack()

  #_____________________________________________________________________________________#
  #_____________________________________________________________________________________#
    submit_button.pack(side='bottom')
    group_booking_checkbox.pack(side='bottom')

    # Update the scrollregion after starting 'mainloop'
    # when all widgets are created
    checkbutton_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    window.mainloop()

if __name__ == "__main__":
    pass


# Create a table to store bookings
cursor.execute('''CREATE TABLE IF NOT EXISTS bookings (
                    SR_NO INTEGER PRIMARY KEY AUTOINCREMENT,
                    time_slot TEXT,
                    booking_date DATE,
                    payable_amount REAL,
                    turf_id INTEGER,
                    booking_amount INT,
                    turf_name TEXT
                )''')
def book_slot(time_slot, booking_date, payable_amount, booking_amount, turf_name):
    # Generate a random turf ID
    turf_id = random.randint(10009, 99999)
    # Insert the booking details into the table
    cursor.execute('''INSERT INTO bookings (time_slot, booking_date, payable_amount, turf_id, booking_amount, turf_name) 
                      VALUES (?, ?, ?, ?, ?, ?)''', (time_slot, booking_date, payable_amount, turf_id, booking_amount, turf_name))
    conn.commit()
    print("Booking successful. Turf ID:", turf_id)
    
root = Tk()   
group_booking_var = StringVar()
global time_entry
time_entry = Entry(root)
time_entry.pack()


date_entry = Entry(root)
date_entry.pack()

payable_entry = Entry(root)
payable_entry.pack()

entry_4 = Entry(root)
entry_4.pack()
current_user_id = None

def get_current_user_id():
    with sqlite3.connect("build\\user.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT MAX(id) FROM current_user")
        result = cursor.fetchone()
        if result is not None:
            return result[0]
        else:
            print("No users found")
            return None

def get_wallet_balance(user_id):
    with sqlite3.connect("build\\user.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT wallet FROM current_user WHERE id = ?", (user_id,))
        result = cursor.fetchone()
        if result is not None:
            wallet_balance = result[0]
            print(f"Wallet balance: {wallet_balance}")
            return wallet_balance
        else:
            print("No user found with given ID")
            return None

#ad
def store_values():
    
    if time_entry:
        time_slot = time_entry.get()
        booking_date = date_entry.get()
        
        group_booking = group_booking_var.get() 
        current_user_id = get_current_user_id()  #  user ID
        wallet_balance = get_wallet_balance(current_user_id)  
        print(f"Current user ID: {current_user_id}")  # Print the current user ID
        wallet_balance = get_wallet_balance(current_user_id)  
        print(group_booking_var.get())
        print(f"Current wallet balance: {wallet_balance}")
        
        cursor.execute("SELECT name FROM current_user ORDER BY id DESC LIMIT 1")
        name_row = cursor.fetchone()
        if name_row is None:
            messagebox.showerror("Error", "No name found in the current user table.")
            return
        turf_name = name_row[0]
        
        try:
            payable_amount = float(payable_entry.get())  
            booking_amount = float(entry_4.get())  
        except ValueError:
            messagebox.showerror("Error", "Payable amount and booking amount must be numbers.")
            return

        if not time_slot:
            messagebox.showerror("Error", "Time slot must be filled.")
            return

        if not booking_date:
            messagebox.showerror("Error", "Booking date must be filled.")
            return

        if payable_amount is None:
            messagebox.showerror("Error", "Payable amount must be filled.")
            return

        if booking_amount is None:
            messagebox.showerror("Error", "Booking amount must be filled.")
            return
        
        print(f'group_booking: {group_booking}, payable_amount: {payable_amount}, booking_amount: {booking_amount}')
        # Assuming `window` is the instance of your window
        if group_booking == "":
            try:
                if (payable_amount) != (booking_amount):
                    messagebox.showerror("Error", "For group booking, payable amount should not be equal to booking amount.")
                    return
            except ValueError:
                messagebox.showerror("Error", "Payable amount and booking amount must be numbers.")
                return

        print(f"Time slot: {time_slot}, Booking date: {booking_date}, Payable amount: {payable_amount}, Booking amount: {booking_amount}, Group booking: {group_booking}")  # New print statement

        # Generate a random turf ID
        turf_id = "TF" + str(random.randint(9999, 99990))
        # Insert the booking details into the table
        cursor.execute('''INSERT INTO bookings (time_slot, booking_date, payable_amount, turf_id, booking_amount, turf_name) 
                  VALUES (?, ?, ?, ?, ?, ?)''', (time_slot, booking_date, payable_amount, turf_id, booking_amount, turf_name))
        conn.commit()
        
        print("Booking succe\
            ssful. Turf ID:", turf_id)
        messagebox.showinfo("Success", "Booking successful. Turf ID: " + str(turf_id))

        # Destroy the window after successful booking
        window.destroy()

        print(f"Time slot: {time_slot}, Booking date: {booking_date}, Payable amount: {payable_amount}, Booking amount: {booking_amount}, Group booking: {group_booking}")  # New print statement

        

        # Generate a random turf ID
        turf_id = "TF" + str(random.randint(9999, 99990))
        # Insert the booking details into the table
        cursor.execute('''INSERT INTO bookings (time_slot, booking_date, payable_amount, turf_id, booking_amount) 
                          VALUES (?, ?, ?, ?, ?)''', (time_slot, booking_date, payable_amount, turf_id, booking_amount))
        conn.commit()
        print("Booking successful. Turf ID:", turf_id)
        messagebox.showinfo("Success", "Booking successful. Turf ID: " + str(turf_id))
    else:
        print("Time entry widget is not available.")
        
root.mainloop()
    
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"G:\TurfBookingSyS\build\assets\frame2")

def open_date_picker(date_entry):
    # Create a new window
    date_picker_window = Toplevel(window)

    # Create a DateEntry widget
    date_entry_widget = DateEntry(date_picker_window, date_pattern='dd/mm/yyyy')
    date_entry_widget.pack()

    # Add a command to set the date_entry widget's text to the selected date
    def on_date_selected(event):
        date_entry.delete(0, 'end')  # clear the date_entry widget
        date_entry.insert(0, date_entry_widget.get())  # insert the selected date

    date_entry_widget.bind("<<DateEntrySelected>>", on_date_selected)
def open_booking():
    global time_entry,date_entry,payable_entry,entry_4
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"G:\TurfBookingSyS\build\assets\frame2")

    
    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    
    window = Toplevel()
    

    window.geometry("386x390")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 390,
        width = 386,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_11.png"))
    entry_bg_1 = canvas.create_image(
        100.5,
        274.0,
        image=entry_image_1
    )
#payable 
    payable_entry = Entry(
        window,
        bd=0,
        bg="#FFC83D",
        fg="#000716",
        highlightthickness=0
    )
    payable_entry.place(
        x=43.0,
        y=254.0,
        width=115.0,
        height=38.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_11.png"))
    image_1 = canvas.create_image(
        339.0,
        150.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_21.png"))
    image_2 = canvas.create_image(
        339.0,
        206.0,
        image=image_image_2
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_21.png"))
    entry_bg_2 = canvas.create_image(
        191.5,
        206.0,
        image=entry_image_2
    )
    #select time
    time_entry = Entry(window,
        bd=0,
        bg="#FFC83D",
        fg="#000716",
        highlightthickness=0
    )
    time_entry.place(
        x=62.0,
        y=186.0,
        width=259.0,
        height=38.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_31.png"))
    entry_bg_3 = canvas.create_image(
        191.5,
        150.0,
        image=entry_image_3
    )
    #select date
    date_entry= Entry(window,
        bd=0,
        bg="#FFC83D",
        fg="#000716",
        highlightthickness=0
    )
    date_entry.place(
        x=62.0,
        y=130.0,
        width=259.0,
        height=38.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_41.png"))
    entry_bg_4 = canvas.create_image(
        290.5,
        274.0,
        image=entry_image_4
    )
    entry_4 = Entry(window,
        bd=0,
        bg="#FFC83D",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=233.0,
        y=254.0,
        width=115.0,
        height=38.0
    )
    global button_store
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_11.png"))
    button_store = Button(window,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=store_values,
        relief="flat",
        bg="#ffffff"
    )
    button_store.place(
        x=127.0,
        y=321.0,
        width=132.0,
        height=45.0
    )

    canvas.create_rectangle(
        1.0,
        0.0,
        389.0,
        92.0,
        fill="#E4E8F2",
        outline="")

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_21.png"))
    button_2 = Button(window,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_time_slots_window(time_entry, payable_entry),
        # lambda: print("button_2 time -clicked"),
        relief="flat",
        bg="#ffffff"
    )
    button_2.pack()
    button_2.place(
        x=20.0,
        y=187.0,
        width=41.0,
        height=50.0
    )

    canvas.create_rectangle(
        -2.9993742782316986,
        88.0,
        386.0012514435366,
        92.06121801720494,
        fill="#000000",
        outline="")

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_31.png"))
    button_3 = Button(window,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_date_picker(date_entry),
        # lambda: print("button_3 date clicked"),
        relief="flat",
        bg="#ffffff"
    )
    button_3.place(
        x=20.0,
        y=130.0,
        width=41.0,
        height=40.0
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_51.png"))
    entry_bg_5 = canvas.create_image(
        192.5,
        52.0,
        image=entry_image_5
    )
    entry_5 = Entry(window,
        bd=0,
        bg="#E4E9F2",
        fg="#000716",
        highlightthickness=0
    )
    entry_5.place(
        x=49.0,
        y=29.0,
        width=287.0,
        height=44.0
    )

    canvas.create_text(
        62.0,
        113.0,
        anchor="nw",
        text="Select Date",
        fill="#000000",
        font=("Poppins SemiBold", 12 * -1)
    )

    canvas.create_text(
        62.0,
        169.0,
        anchor="nw",
        text="Select Time",
        fill="#000000",
        font=("Poppins SemiBold", 12 * -1)
    )

    canvas.create_text(
        38.0,
        236.0,
        anchor="nw",
        text="Payable Amt.",
        fill="#000000",
        font=("Poppins SemiBold", 12 * -1)
    )
    canvas.create_text(
        225.0,
        236.0,
        anchor="nw",
        text="Booking Amt.",
        fill="#000000",
        font=("Poppins SemiBold", 12 * -1)
    )

    window.resizable(False, False)
    window.update_idletasks()
    
    window.mainloop()
#@@@@@@@@@@@@@@@ 
#____________________________##------------------#

def open_grp_booking():
    window.withdraw()
    call(["python","build\\groupbook.py"])
    window.deiconify()
def open_calander():
    window.withdraw()
    call(["python","build\\calander.py"])
    window.deiconify()
    
def open_account():
    window.withdraw()
    call(["python","build\\account.py"])
    window.deiconify()
def open_event():
    window.withdraw()
    call(["python","build\\event.py"])
    window.deiconify()
def open_mybooking():
    window.withdraw()
    call(["python","build\\mybooking.py"])
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
    command=lambda: print("button_1_321 clicked"),
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
    command=open_calander,
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
    command=open_event,
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
    command=open_mybooking,
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
    command=open_account,
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
    command=open_booking,
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
    command=open_booking,
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
    command= open_booking,
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
