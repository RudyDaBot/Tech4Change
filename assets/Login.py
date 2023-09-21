from tkinter import *
from tkinter import messagebox
import subprocess

root = Tk ()
root.title ('Log in / Sign in')
root.geometry ("925x500")
root.resizable (False, False)
root.config(bg='white')



# LOGIN PAGE --------------------------------------------------------------------------------------------------------------------------
# LOGIN PAGE --------------------------------------------------------------------------------------------------------------------------

head = Label (root, text = "Tech4Change", bg='white', foreground='#03254C')
head.config (font = ('Microsoft YaHei UI Light', 30))
head.place(x=475,y=70)

# Enter Username

user = Entry(width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 9))
user.place(x=480,y=170)
user.insert(0, "Username")
underline_u = Frame(width=300, height=2, bg='black')
underline_u.place(x=470,y=194)

def clickInU(e) :
    user.delete(0,'end')
def clickOutU(e) :
    userUsername = user.get()
    if userUsername=='':
        user.insert(0, 'Username')

user.bind('<FocusIn>', clickInU)
user.bind('<FocusOut>', clickOutU)

# Enter Password

password = Entry(width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 9))
password.place(x=480,y=210)
password.insert(0, "Password")
underline_p = Frame(width=300, height=2, bg='black')
underline_p.place(x=470,y=234)

def clickInP(e) :
    password.delete(0,'end')
def clickOutP(e) :
    userPassword = password.get()
    if userPassword=='':
        password.insert(0, 'Password')

password.bind('<FocusIn>', clickInP)
password.bind('<FocusOut>', clickOutP)

# Login Error Displayer

def open_another_script():
    root.quit()
    script_path = 'home.py'
    subprocess.Popen(['python', script_path])

def login():
    global user
    global password
    global appMode
    user_value = user.get()  # Get the current value of the 'user' Entry widget
    password_value = password.get()  # Get the current value of the 'password' Entry widget
    if user_value == 'user' and password_value == 'tech4change':
        open_another_script()
    else:
        messagebox.showerror("Error", "Sign Up is currently unavailable. Kindly use user - 'user' and password - 'tech4change' to use the app")


# Sign In Button

button_si = Button(width=37, border=0, text='Sign in', bg='#034A4C', foreground='white', height=2, command=login)
button_si.place(x=470,y=290)
button_si.config(cursor="hand2")

# No Account Text And Button

noATxt = Label(text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
noATxt.place(x=510,y=360)

SUbtn = Button(width=6, text='Sign up', border=0, bg='white', foreground='#03254C', command=login)
SUbtn.place(x=665, y=358)
SUbtn.config(cursor="hand2")


root.mainloop() 
