# import Database as Db
import tkinter as tk
import datetime as dt

# window settings:
window = tk.Tk()
window.geometry("600x400")
window.title("Teachers Birthdays by Yoav Spiegel and Ido Kedem")

# show today's date on the top abd add a sub-title
randomdate = dt.date(year=2022, month=9, day=22)
today = randomdate.today().strftime("%x")
today = today[3:6] + today[0:3] + today[6:8]
todaymsg = tk.Label(window, text="Today: " + today, font=("arial", 20))
todaymsg.pack()
whohasbd = tk.Label(window, text="The teachers who have a birthday today are: ", font=("arial", 12), pady=10)
whohasbd.pack()


general_BDays = {"29/09": ["Ani Ido Kedem"], "26/07": ["Yoav Spiegel"], "23/09": ["nobody", "no one"]}  # until real one

teachers_label_text = ""
for date in general_BDays:
    if date == today[0:5]:
        for teacher in general_BDays[date]:
            teachers_label_text += teacher + "\n"
teachers_label = tk.Label(window, text=teachers_label_text, font=("arial", 10))
teachers_label.pack()

window.mainloop()
