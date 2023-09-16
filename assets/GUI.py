from tkinter import *

window=Tk()

def bruh() :
    print("BRUH")


# this is a button
btn=Button(window, text="click me daddy", fg='black', font=('Comic Sans MS', 10), command=bruh)
btn.place(x=80, y=100)

# this is a label
lbl=Label(window, text="oh yes daddy oh yeah", fg='black', font=("Comic Sans MS", 16))
lbl.place(x=60, y=50)

# this is a entry box
txtfld=Entry(window, text="enter in to me daddy", bd=5, font=("Comic Sans MS", 10))
txtfld.place(x=80, y=150)


# this is some setup to render those things
window.title('Tech4Change')
window.geometry("300x200+10+10")
window.mainloop()