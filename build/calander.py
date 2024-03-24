
import calendar
from pathlib import Path
import json
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
from datetime import date
from tkinter import ttk
import sqlite3
from calendar import monthrange
conn=sqlite3.connect(r'build/user.db')
cursor=conn.cursor()
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"G:\TurfBookingSyS\build\assets\frame4")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Calendar")

window.geometry("1340x740")
window.configure(bg = "#000000")
#______________________________-  @@@@@@@@  -______________________________#
class CalendarApp(tk.Frame):
    def book_appointment(self, day, month, day_of_week):
        try:
            conn = sqlite3.connect(r'build/user.db')
            cursor = conn.cursor()
            booking_date = date(self.year, month, day)  # Use the selected year, month, and day
            booking_date_str = booking_date.strftime("%d/%m/%Y")  # Corrected date format
            print(f"Booking date: {booking_date_str}")  # Print the booking date to the terminal
            # Fetch the time_slot from the bookings table
            cursor.execute("SELECT time_slot FROM bookings WHERE booking_date = ?", (booking_date_str,))
            time_slot_row = cursor.fetchone()
            print(f"Query result: {time_slot_row}")  # Print the result of the query to the terminal
            if time_slot_row is not None:
                time_slot = time_slot_row[0]
                print(f"Time slot:\n\{time_slot}")  # Print the time slot in the terminal
                # Update the text box with the time_slot
                self.time_slot_text_box.delete("1.0", tk.END)
                self.time_slot_text_box.insert("1.0", f"\t\tTime slot:\n\n {time_slot}")
                self.text_object_dict[day].delete("1.0", tk.END)
                self.text_object_dict[day].tag_configure("black", foreground="black")
                self.text_object_dict[day].insert("1.0", f"Appointment booked on {day_of_week}, {day}")
            else:
                print("No time slot found for the given date.")
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if conn:
                conn.close()

    #___________________________________#
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        # Create a connection to the database
        # Create a connection to the database
        # self.conn = sqlite3.connect('appointments.db')
        self.conn = sqlite3.connect(r'build/user.db')
        self.c = self.conn.cursor()
        self.time_slot_text_box = tk.Text(window, width=44, height=25,fg="blue",font=('Arial', 13, 'bold'))
        self.time_slot_text_box.place(x=917, y=140)
        # # Create a cursor
        # self.c = self.conn.cursor()

        # # Create a table to store the appointments
    
        # self.c.execute('''
        # CREATE TABLE IF NOT EXISTS appointments (
        # day INTEGER,
        # date_of_booking TEXT,
        # appointment TEXT,
        # day_of_week TEXT,
        # month INTEGER
        #  )
        #     ''')
      
        # self.conn.commit()
        
        # Commit the changes
        
      
#___________________________________#
        style = ttk.Style()
        self.configure(bg='white')
        self.month = date.today().month
        self.year = date.today().year
        self.save_dict = {}
        self.text_object_dict = {}
        
      
        
        self.columnconfigure(0, weight=1)

        self.calendar_frame = tk.Frame(self, bg='white')
        self.calendar_frame.grid()
        
        self.print_month_year(self.month, self.year)
        self.make_buttons()
        self.month_generator(self.day_month_starts(self.month, self.year), self.days_in_month(self.month, self.year))

    def print_month_year(self, month, year):
        
        month_names = [
            "January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"
        ]

        written_month = month_names[month - 1]
        month_year_label = tk.Label(self.calendar_frame, text=f"{written_month} {year}", bg="white", fg='#064ACB', font=("Arial", 25, "bold"), anchor='center')
        month_year_label.grid(column=0, row=0, columnspan=7, pady=(20, 0), sticky='ew')

    def switch_months(self, direction):
        if self.month == 12 and direction == 1:
            self.month = 0
            self.year += 1
        if self.month == 1 and direction == -1:
            self.month = 13 
            self.year -= 1

        self.text_object_dict.clear()
        self.save_dict.clear()

        self.calendar_frame.destroy()
        self.calendar_frame = tk.Frame(self, bg='white')
        self.calendar_frame.grid()
        self.month += direction
        self.print_month_year(self.month, self.year)
        self.make_buttons()
        self.month_generator(self.day_month_starts(self.month, self.year), self.days_in_month(self.month, self.year))

    def make_buttons(self):
        go_back_button = tk.Button(self.calendar_frame, text="<", command=lambda: self.switch_months(-1), height=1, width=3,bg='#064ACB', fg='white',font=("Arial", 12, "bold"))
        go_back_button.grid(column=1, row=0,pady=(10, 0))
        go_forward_button = tk.Button(self.calendar_frame, text=">", command=lambda: self.switch_months(1), height=1, width=3, bg='#064ACB', fg='white',font=("Arial", 12, "bold"))
        go_forward_button.grid(column=5, row=0,pady=(10, 0))

        go_back_year_button = tk.Button(self.calendar_frame, text="<<", command=self.decrease_year, height=1, width=3, bg='#064ACB', fg='white',font=("Arial", 12, "bold"))
        go_back_year_button.grid(column=0, row=0,pady=(10, 0))
        go_forward_year_button = tk.Button(self.calendar_frame, text=">>", command=self.increase_year, height=1, width=3, bg='#064ACB', fg='WHITE',font=("Arial", 12, "bold"))
        go_forward_year_button.grid(column=6, row=0,pady=(10, 0))

    def decrease_year(self):
        self.year -= 1
        self.switch_months(0)

    def increase_year(self):
        self.year += 1
        self.switch_months(0)

    def month_generator(self, start_date, number_of_days):
        day = 1 
        # Connect db user
        conn=sqlite3.connect(r'build/user.db')
        cursor=conn.cursor()
    
        cursor.execute("SELECT  booking_date FROM bookings")
        booking_dates = cursor.fetchall()
        appointment_dates = {row[0] for row in booking_dates}
        print("Booking dates:", booking_dates)
        print("Appointment dates:", appointment_dates)
        day_names = ["Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"]

        for name_number in range(len(day_names)):
            day_label = tk.Label(self.calendar_frame, text=day_names[name_number], fg="white", font=("Arial", 12, "bold"), bg='#064ACB')
            day_label.grid(column=name_number, row=0, sticky='nsew', pady=(80, 0))
            self.calendar_frame.columnconfigure(name_number, weight=1,uniform="equal")  # Add this line

        num_days = calendar.monthrange(self.year, self.month)[1]
        index = 0
        day = 1
        # Adjust the month value
    # Adjust the month value
        self.month = self.month if self.month <= 12 else 1

        num_days = calendar.monthrange(self.year, self.month)[1]
    # rest of your code
        # rest of your code
        for row in range(6):
                for column in range(7):
                    if index >= start_date and index <= start_date + num_days - 1:
                        if day <= num_days:
                            current_date = date(self.year, self.month, day)
                            current_date_str = current_date.strftime('%d/%m/%Y')
                            day_of_week = current_date.strftime('%A')
                            day_frame = tk.Frame(self.calendar_frame, bg='white', bd=1, relief='groove', highlightbackground="blue")
                            day_frame.grid(row=row + 2, column=column, sticky='nsew')

                            text_box = tk.Text(day_frame, width=3, height=0.1, font=("Verdana", 12, "bold"), bg='white', fg='red')
                            text_box.grid(row=1)

                            if current_date_str in appointment_dates:
                                # Insert '@@@@' into the Text widget
                                text_box.insert(tk.END, "@@@@")
                                
                            else:
                                # Insert the day number into the Text widget
                                text_box.insert(tk.END, " ")

                            self.text_object_dict[day] = text_box

                            day_frame.columnconfigure(0, weight=1)
                            day_number_label = tk.Label(day_frame, text=day, font=("Verdana", 10, "bold"), bg='white', fg='#064ACB')
                            day_number_label.grid(row=0, sticky='nw')

                            book_button = tk.Button(day_frame, text="Book", command=lambda day=day, month=self.month, day_of_week=day_of_week: self.book_appointment(day, month, day_of_week))
                            book_button.grid(row=2)

                            day += 1
                    index += 1

        load_from_button = tk.Button(self.calendar_frame, text="Load month from...", command=self.load_from_json, bg='white', fg='white')
        save_to_button = tk.Button(self.calendar_frame, text="Save month to...", command=self.save_to_json, bg='white', fg='white')

        load_from_button.grid(row=8, column=4, pady=(40, 0))
        save_to_button.grid(row=8, column=2, pady=(40, 0))

    def save_to_json(self):
        for day in range(len(self.text_object_dict)):
            self.save_dict[day] = self.text_object_dict[day + 1].get("1.0", "end - 1 chars")

        file_location = filedialog.asksaveasfilename(initialdir="/", title="Save JSON to..")
        if file_location != '':
            with open(file_location, 'w') as j_file:
                json.dump(self.save_dict, j_file)

    def load_from_json(self):
        file_location = filedialog.askopenfilename(initialdir="/", title="Select a JSON to open")
        if file_location != '':
            with open(file_location) as f:
                self.save_dict = json.load(f)

                for day in range(len(self.text_object_dict)):
                    self.text_object_dict[day + 1].insert("1.0", self.save_dict[str(day)])

    def is_leap_year(self, year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def day_month_starts(self, month, year):
        lastTwoYear = year - 2000
        calculation = lastTwoYear // 4
        calculation += 1
        if month == 1 or month == 10:
            calculation += 1
        elif month == 2 or month == 3 or month == 11:
            calculation += 4
        elif month == 5:
            calculation += 2
        elif month == 6:
            calculation += 5
        elif month == 8:
            calculation += 3
        elif month == 9 or month == 12:
            calculation += 6
        else:
            calculation += 0
        leapYear = self.is_leap_year(year)
        if leapYear and (month == 1 or month == 2):
            calculation -= 1
        calculation += 6
        calculation += lastTwoYear
        dayOfWeek = calculation % 7
        return dayOfWeek

    def days_in_month(self, month, year):
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 12 or month == 10:
            numberDays = 31
        elif month == 4 or month == 6 or month == 9 or month == 11:
            numberDays = 30
        else:
            leapYear = self.is_leap_year(year)
            if leapYear:
                numberDays = 29
            else:
                numberDays = 28
        return numberDays


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
    483.0,
    70.0,
    anchor="nw",
    text="CALENDAR",
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

canvas.create_rectangle(
    914.0,
    16.0,
    1321.0,
    724.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    1007.0,
    70.0,
    anchor="nw",
    text="BOOKING",
    fill="#020000",
    font=("Poppins SemiBold", 50 * -1)
)

calendar_app = CalendarApp(window)
calendar_app.place(x=340, y=150, width=540, height=560)

# Start the main event loop

window.resizable(False, False)
window.mainloop()