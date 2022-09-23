# import Database as Db
import tkinter as tk
import datetime as dt

# window settings:
window = tk.Tk()
window.geometry("600x400")
window.title("Teachers Birthdays by Yoav Spiegel and Ido Kedem")

def format_date(input_date):
    formatted = input_date.strftime("%x")
    return formatted[3:6] + formatted[0:2]


# First part: initialisation of basic screen and variables

random_date = dt.date(year=2022, month=9, day=22)
global current_date
current_date = random_date.today()
date_label = tk.Label(window, text=format_date(current_date), font=("arial", 20))
date_label.place(x=270, y=300)
# tomorrow = current_date + dt.timedelta(days=1)
today = format_date(current_date)
who_has_bd = tk.Label(window, text="Teachers who have a birthday today: ", font=("arial", 20), pady=10)
who_has_bd.pack()


general_BDays = {"29/09": ["Ani Ido Kedem"], "26/07": ["Yoav Spiegel"], "25/09": ["nobody", "no one"]}  # until real one

teachers_label_text = ""

for date in general_BDays:
    if date == today:
        for teacher in general_BDays[date]:
            teachers_label_text += teacher + "\n"


teachers_label = tk.Label(window, text=teachers_label_text, font=("arial", 12))
teachers_label.pack()

# Second part: functions for buttons

def update_to_date():
    global current_date
    teachers_label_text = ""

    if current_date == random_date.today():  # return to basic format
        who_has_bd.configure(text="Teachers who have a birthday today: ")

        for date in general_BDays:
            if date == today[0:5]:
                for teacher in general_BDays[date]:
                    teachers_label_text += teacher + "\n"

    else:  # update the title and list according to the changed date
        formatted_date = format_date(current_date)
        who_has_bd.configure(text="Teachers who have a birthday on " + formatted_date)

        for date in general_BDays:
            if date == formatted_date[0:5]:
                for teacher in general_BDays[date]:
                    teachers_label_text += teacher + "\n"

    teachers_label.configure(text=teachers_label_text)


def update_to_month(month, month_name):
    who_has_bd.configure(text="Teachers who have a birthday on " + month_name)

    teachers_label_text = ""
    for date in general_BDays:
        if date[3:] == month:
            for teacher in general_BDays[date]:
                teachers_label_text += teacher + "\n"
    teachers_label.configure(text=teachers_label_text)


def minus_day():
    global current_date
    current_date -= dt.timedelta(days=1)
    update_to_date()


def plus_day():
    global current_date
    current_date += dt.timedelta(days=1)
    update_to_date()


# Third part: buttons and date interface

minus_day = tk.Button(window, text="⮝", width=4, height=2, command=minus_day())
minus_day.place(x=225, y=300)

plus_day = tk.Button(window, text="⮟", width=4, height=2, command=plus_day())
plus_day.place(x=350, y=300)

window.mainloop()
