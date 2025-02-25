#login app

from tkinter import *
root = Tk()
root.title('Act2-Login App')
root.geometry('400x400')
frame = Frame(master=root, height=200, width=360, bg="pink")
label1 = Label(frame, text="Email Id", width=12)
label2 = Label(frame, text="Enter Password",width=12)
email_ip= Entry(frame)
pass_ip = Entry(frame, show="*")

def display():
	message = "You have created new account!"
	textbox.insert(END, message)

textbox = Text( fg="black")
btn = Button(text="Create Account", command=display, bg="blue")
frame.place(x=20, y=0)
label1.place(x=20, y=80)
email_ip.place(x=150, y=80)
label2.place(x=20, y=140)
pass_ip.place(x=150, y=140)
btn.place(x=130, y=210)
textbox.place(y=250)
root.mainloop()
