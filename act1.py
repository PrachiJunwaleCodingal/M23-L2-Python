#number pad

from tkinter import *

root = Tk()
root.title('Act1-Number Pad')
root.geometry('230x300')
n = [[9, 8, 7], [6, 5, 4], [3, 2, 1], ['#', 0, '*']]

for i in range(4):
	root.columnconfigure(i, weight=1, minsize=75)
	root.rowconfigure(i, weight=1, minsize=50)

for i in range(4):
	for j in range(3):
		frame = Frame(master=root,relief=RAISED,borderwidth=1,bg="pink")
		frame.grid(row=i, column=j, sticky="nsew") #north south east west
		label = Label(master=frame, text=n[i][j], bg='yellow', font=('Arial',16))
		label.pack(expand=True, fill='both', padx=5, pady=5)

root.mainloop()
