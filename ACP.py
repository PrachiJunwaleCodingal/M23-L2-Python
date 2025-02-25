#age calculator
from tkinter import *
from datetime import datetime
root = Tk()
root.title('Age calculator App')
root.geometry('400x400')
frame = Frame(master=root, height=300, width=360, bg="pink")
label1 = Label(frame, text="Enter birth date", width=12)
label2 = Label(frame, text="Enter birth month",width=12)
label3 = Label(frame, text="Enter birth year",width=12)

date_ip= Entry(frame)
month_ip= Entry(frame)
year_ip= Entry(frame)


def display():
    day = int(date_ip.get())
    month = int(month_ip.get())
    year = int(year_ip.get())
    birth_date = datetime(year, month, day)
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    age_label.config(text=f"Your age is: {age} years")



btn = Button(text="Age calculator", command=display, bg="blue")

frame.place(x=20, y=0)
label1.place(x=20, y=80)
date_ip.place(x=150, y=80)
label2.place(x=20, y=140)
month_ip.place(x=150, y=140)
label3.place(x=20, y=210)
year_ip.place(x=150, y=210)
btn.place(x=130, y=320)

age_label =Label(root, text="")

age_label.place(x=80,y=350)
root.mainloop()

