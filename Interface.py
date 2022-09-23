import Database as db
import tkinter as tk
import datetime as dt

# window settings:
window = tk.Tk()
window.geometry("600x400")
window.title("Teachers Birthdays by Yoav Spiegel and Ido Kedem")

# show today's date on the top abd add a sub-title
random_date = dt.date(year=2022, month=9, day=22)
today = random_date.today().strftime("%x")
today = today[3:6] + today[0:3] + today[6:8]
today_msg = tk.Label(window, text="Today: " + today, font=("arial", 20))
today_msg.pack()
who_has_bd = tk.Label(window, text="Teachers who have a birthday today: ", font=("arial", 12), pady=10)
who_has_bd.pack()


general_BDays = db.load_database_dict()

teachers_label_text = ""
for date in general_BDays:
    if date == today[0:5]:
        for teacher in general_BDays[date]:
            teachers_label_text += teacher + "\n"

teachers_label = tk.Label(window, text=teachers_label_text, font=("arial", 10))
teachers_label.pack()

window.mainloop()
