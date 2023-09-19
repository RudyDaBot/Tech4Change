from tkinter import *

window=Tk()
window.title('Tech4Change')
window.geometry("800x730")

def bruh() :
    print("BRUH")

coordsX = window.winfo_screenwidth()
coordsY = window.winfo_screenheight()

# this is a button
btn=Button(window, text="click me daddy", fg='black', font=('Comic Sans MS', 10), command=bruh)
btn.place(x=coordsX/2, y=coordsY)

# this is a label
lbl=Label(window, text="oh yes daddy oh yeah", fg='black', font=("Comic Sans MS", 16))
lbl.place(x=coordsX/2, y=coordsY/2)

# this is a entry box
txtfld=Entry(window, text="enter in to me daddy", bd=5, font=("Comic Sans MS", 10))
txtfld.place(x=180, y=250)

window.mainloop()

while (True) :
    print(coordsX, coordsY)


# this is some setup to render those things

