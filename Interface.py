import Database as db
import tkinter as tk
import datetime as dt


window = tk.Tk()
window.geometry("600x600")
window.title("Teachers Birthdays by Yoav Spiegel and Ido Kedem")


def format_date(input_date):
    formatted = input_date.strftime("%d/%m")
    return formatted


# First part: initialisation of basic screen and variables

random_date = dt.date(year=2022, month=9, day=22)

window.current_date = random_date.today()
date_label = tk.Label(window, text=format_date(window.current_date), font=("arial", 20), pady=20)
date_label.pack()
today = format_date(window.current_date)

window.general_BDays = db.load_database_dict()

teachers_label_text = ""

for date in window.general_BDays:  # show only teachers born today
    if date == today:
        for teacher in window.general_BDays[date]:
            teachers_label_text += teacher + "\n"

teachers_label = tk.Label(window, text=teachers_label_text, font=("arial", 12))
teachers_label.pack()


# Second part: date buttons


def update_to_date():
    """
    Uses the current date to show the correct messages in every label concerning it
    Activated by plus_day and minus_day buttons
    :return: None
    """
    teachers_label_text = ""

    formatted_date = format_date(window.current_date)
    date_label.configure(text=formatted_date)

    for date in window.general_BDays:
        if date == formatted_date[0:5]:
            for teacher in window.general_BDays[date]:
                teachers_label_text += teacher + "\n"

    teachers_label.configure(text=teachers_label_text)


def minus_day():  # go a day backwards and update
    window.current_date -= dt.timedelta(days=1)
    update_to_date()


def plus_day():  # go one day forward and update
    window.current_date += dt.timedelta(days=1)
    update_to_date()


plus_day = tk.Button(window, text="⮝", width=4, height=2, command=plus_day)
plus_day.place(x=220, y=20)

minus_day = tk.Button(window, text="⮟", width=4, height=2, command=minus_day)
minus_day.place(x=340, y=20)


def mode_change():  # update state to present by date and retrieve plus/minus day buttons (kill button too)
    update_to_date()
    return_to_date_mode.pack_forget()
    plus_day.place(x=220, y=20)
    minus_day.place(x=340, y=20)


return_to_date_mode = tk.Button(window, text="Return to date mode", command=mode_change)


# Third part: month buttons

def update_to_month(month, month_name):
    """
    Used by the 12 month buttons
    Updates the teachers list according to the month parameters
    Deletes plus/minus buttons and adds mode change button
    :param month: two-digit number to sort dates by
    :param month_name: the name that shall be presented on the main label
    :return: None
    """
    date_label.configure(text=month_name + " Birthdays")

    teachers_label_text = ""
    for date in window.general_BDays:
        if date[3:] == month:
            for teacher in window.general_BDays[date]:
                teachers_label_text += date + " " + teacher + "\n"
    teachers_label.configure(text=teachers_label_text)
    return_to_date_mode.pack()

    plus_day.place_forget()
    minus_day.place_forget()


jan = tk.Button(window, text="January", command=lambda: update_to_month("01", "January"), width=10)
jan.place(x=25, y=75)
feb = tk.Button(window, text="February", command=lambda: update_to_month("02", "February"), width=10)
feb.place(x=25, y=125)
mar = tk.Button(window, text="March", command=lambda: update_to_month("03", "March"), width=10)
mar.place(x=25, y=175)
apr = tk.Button(window, text="April", command=lambda: update_to_month("04", "April"), width=10)
apr.place(x=25, y=225)
may = tk.Button(window, text="May", command=lambda: update_to_month("05", "May"), width=10)
may.place(x=25, y=275)
jun = tk.Button(window, text="June", command=lambda: update_to_month("06", "June"), width=10)
jun.place(x=25, y=325)

jul = tk.Button(window, text="July", command=lambda: update_to_month("07", "July"), width=10)
jul.place(x=495, y=75)
aug = tk.Button(window, text="August", command=lambda: update_to_month("08", "August"), width=10)
aug.place(x=495, y=125)
sep = tk.Button(window, text="September", command=lambda: update_to_month("09", "September"), width=10)
sep.place(x=495, y=175)
oct = tk.Button(window, text="October", command=lambda: update_to_month("10", "October"), width=10)
oct.place(x=495, y=225)
nov = tk.Button(window, text="November", command=lambda: update_to_month("11", "November"), width=10)
nov.place(x=495, y=275)
dec = tk.Button(window, text="December", command=lambda: update_to_month("12", "December"), width=10)
dec.place(x=495, y=325)


# Fourth part: extra functions ADD and SEARCH

def add_screen():
    add_window = tk.Tk()
    add_window.geometry("200x200")
    add_window.title("Add a teacher")

    name_label = tk.Label(add_window, text="Name: ", font=("arial", 8))
    name_label.place(x=15, y=20)
    name = tk.Entry(add_window, width=20)
    name.place(x=55, y=20)

    date_label = tk.Label(add_window, text="Date: ", font=("arial", 8))
    date_label.place(x=15, y=60)
    day = tk.Spinbox(add_window, from_=1, to=31, width=6)
    month = tk.Spinbox(add_window, from_=1, to=12, width=6)
    day.place(x=55, y=60)
    month.place(x=130, y=60)
    slash = tk.Label(add_window, text="/", font=('arial', 12))
    slash.place(x=113, y=58)

    error_label = tk.Label(add_window, text="", font=("arial", 10), fg="red")
    error_label.pack(side='bottom', pady=2)

    def submit_and_add():
        month_days = {
            "1": '31',
            "2": '29',
            "3": '31',
            "4": '30',
            "5": '31',
            "6": '30',
            "7": '31',
            "8": '31',
            "9": '30',
            "10": '31',
            "11": '30',
            "12": '31'
        }
        day_val: str = day.get()
        month_val: str = month.get()
        name_val: str = name.get()

        error_text = ""

        if not (day_val.isnumeric() and month_val.isnumeric()):
            error_text += "Date must be numeric\n"

        elif day_val > month_days[month_val]:
            error_text += "Invalid date\n"

        if name_val == "":
            error_text += "Name must have value\n"

        elif name_val.isnumeric():
            error_text += "Name must be a word\n"

        elif db.is_duplicate_teacher(name_val):
            error_text += "Teacher already exists\n"

        error_label.configure(text=error_text)

        if error_text == "":
            db.add_teacher_to_db(f"{day_val}/{month_val}", name_val)
            window.general_BDays = db.load_database_dict()
            window.update()
            add_window.destroy()


    submit = tk.Button(add_window, text="Add", command=submit_and_add)
    submit.pack(side='bottom', pady=5)

    add_window.mainloop()


def search_screen():
    search_window = tk.Tk()
    search_window.geometry("200x200")
    search_window.title("Search for a teacher")

    entry_title = tk.Label(search_window, text="Enter your search: ", font=('arial', 10))
    entry_title.pack(side='top', pady=2)

    search_bar = tk.Entry(search_window)
    search_bar.pack(side='top',pady=2)

    results_label = tk.Label(search_window, text="", font=('arial', 8))
    results_label.pack(side='bottom')

    def submit_and_search():
        results_dict = db.search_teachers(search_bar.get())
        results = ""
        if len(results_dict) == 0:
            results_label.configure(text="No results")
        else:
            for date, names in results_dict.items():
                for name in names:
                    results += f"{name} - {date}\n" if results.count("/") < 30 else ""
            results_label.configure(text=results)

        search_window.geometry(f"200x{100 + results.count('/') * 14}")

    submit = tk.Button(search_window, text="Search", command=lambda: submit_and_search())
    submit.pack(side='top')

    search_window.mainloop()


search = tk.Button(window, text="Search", command=lambda: search_screen(), width=10, height=5)
search.place(x=25, y=425)
add = tk.Button(window, text="Add", command=lambda: add_screen(), width=10, height=5)
add.place(x=495, y=425)

window.mainloop()
