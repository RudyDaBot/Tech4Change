from tkinter import *

window=Tk()

# this is a button
btn=Button(window, text="This is Button widget", fg='blue')
btn.place(x=80, y=100)

# this is a label
lbl=Label(window, text="This is Label widget", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)

# this is a entry box
txtfld=Entry(window, text="This is Entry Widget", bd=5)
txtfld.place(x=80, y=150)

# this is some setup to render those things
window.title('Hello Python')
window.geometry("300x200+10+10")
window.mainloop()