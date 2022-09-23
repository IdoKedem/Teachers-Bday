
import Database as db

import tkinter as tk
import datetime as dt

# window settings:
window = tk.Tk()
window.geometry("600x400")
window.title("Teachers Birthdays by Yoav Spiegel and Ido Kedem")


def format_date(input_date):
    formatted = input_date.strftime("%d/%m")
    return formatted


# First part: initialisation of basic screen and variables

random_date = dt.date(year=2022, month=9, day=22)
global current_date
current_date = random_date.today()
date_label = tk.Label(window, text=format_date(current_date), font=("arial", 20))
date_label.place(x=255, y=300)
# tomorrow = current_date + dt.timedelta(days=1)
today = format_date(current_date)
who_has_bd = tk.Label(window, text="Teachers who have a birthday today: ", font=("arial", 20), pady=10)  # default msg
who_has_bd.pack()


general_BDays = db.load_database_dict()


teachers_label_text = ""

for date in general_BDays:  # show only teachers born today
    if date == today:
        for teacher in general_BDays[date]:
            teachers_label_text += teacher + "\n"


teachers_label = tk.Label(window, text=teachers_label_text, font=("arial", 12))


# Second part: date buttons

def update_to_date():
    """

    Uses the current date to show the correct messages in every label concerning it
    Activated by plus_day and minus_day buttons
    :return: None
    """
    global current_date
    teachers_label_text = ""

    formatted_date = format_date(current_date)
    date_label.configure(text=formatted_date)

    if current_date == random_date.today():  # return to basic format
        who_has_bd.configure(text="Teachers who have a birthday today: ")

        for date in general_BDays:
            if date == today[0:5]:
                for teacher in general_BDays[date]:
                    teachers_label_text += teacher + "\n"

    else:  # update the title and list according to the changed date
        who_has_bd.configure(text="Teachers who have a birthday on " + formatted_date)

        for date in general_BDays:
            if date == formatted_date[0:5]:
                for teacher in general_BDays[date]:
                    teachers_label_text += teacher + "\n"

    teachers_label.configure(text=teachers_label_text)


def minus_day():  # go one day backwards and update
    global current_date
    current_date -= dt.timedelta(days=1)
    update_to_date()


def plus_day():  # go one day forward and update
    global current_date
    current_date += dt.timedelta(days=1)
    update_to_date()


plus_day = tk.Button(window, text="⮝", width=4, height=2, command=plus_day)
plus_day.place(x=210, y=300)

minus_day = tk.Button(window, text="⮟", width=4, height=2, command=minus_day)
minus_day.place(x=335, y=300)


def mode_change():  # update state to present by date and retrieve plus/minus day buttons (kill button too)
    update_to_date()
    return_to_date_mode.place_forget()
    plus_day.place(x=210, y=300)
    minus_day.place(x=335, y=300)


return_to_date_mode = tk.Button(window, text="Return to date mode", command=mode_change)


# Third part: month buttons

def update_to_month(month, month_name):
    """

    Used by the 12 month buttons
    Updates the teachers list according to the month parameters
    Deletes plus/minus buttons and adds mode change button
    :param month: two digit number to sort dates by
    :param month_name: the name that shall be presented on the main label
    :return: None
    """
    who_has_bd.configure(text="Teachers who have a birthday in " + month_name)

    teachers_label_text = ""
    for date in general_BDays:
        if date[3:] == month:
            for teacher in general_BDays[date]:
                teachers_label_text += teacher + "\n"
    teachers_label.configure(text=teachers_label_text)
    return_to_date_mode.place(x=232, y=350)

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


window.mainloop()
