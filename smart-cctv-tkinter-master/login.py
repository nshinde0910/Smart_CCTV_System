from ast import main
from faulthandler import disable
from tkinter import messagebox
from distutils.command import config
import tkinter as tk
import tkinter.font as font
from in_out import in_out
from motion import noise
from rect_noise import rect_noise
from record import record
from PIL import Image, ImageTk
from tkinter import filedialog as fd
import os
import sys

window = tk.Tk()
pyexec = sys.executable
window.title("Login Page")
window.iconphoto(False, tk.PhotoImage(file='mn.png'))
window.geometry('900x650+300+50')
# window.configure(bg='#fff')
window.resizable(False, False)
# window.eval('tk::PlaceWindow . center')


frame1 = tk.Frame(window)


def Open_homepage():

    uname = E1.get()
    password = E2.get()

    if uname == "cctv123" and password == "cctv@123":
        os.system('main.py')
        window.quit()

    else:
        messagebox.showerror("WARNING", "Wrong Username or Password")
        E1.delete('0', tk.END)
        E2.delete('0', tk.END)

    return


def close_window():
    window.quit()
    return


def clear_contents():
    E1.delete('0', tk.END)
    E2.delete('0', tk.END)


label_title = tk.Label(frame1, text="Login Page", fg='#57a1f8', bg='#fff',)
label_font = font.Font(size=30, weight='bold',
                       family='microsoft yahei ui light')
label_title['font'] = label_font
label_title.grid(pady=(10, 10), column=2, row=1)

icon = Image.open('icons/lock.png')
icon = icon.resize((150, 150), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon, bg='#fff')
label_icon.grid(row=4, pady=(5, 10), column=2)

# creating Username
label_uname = tk.Label(frame1, text="Username")
label_font = font.Font(size=15, weight='bold',
                       family='microsoft yahei ui light')
label_uname['font'] = label_font
label_uname.grid(pady=(100, 20), column=1, row=10)

E1 = tk.Entry(frame1, bd=5)
# E1.pack(side=tk.RIGHT)
E1.grid(pady=(100, 20), column=2, row=10)


# creating Password
label_password = tk.Label(frame1, text="Password")
label_font = font.Font(size=15, weight='bold',
                       family='microsoft yahei ui light')
label_password['font'] = label_font
label_password.grid(pady=(5, 10), column=1, row=11)

E2 = tk.Entry(frame1, bd=5, show="*")
# E1.pack(side=tk.RIGHT)
E2.grid(pady=(50, 50), column=2, row=11)


sbmitbtn = tk.Button(frame1, text="Submit", activebackground="green",
                     activeforeground="blue", command=Open_homepage)
sbmitbtn_font = font.Font(size=15, weight='bold',
                          family='microsoft yahei ui light')
sbmitbtn['font'] = sbmitbtn_font
sbmitbtn.grid(pady=(10, 10), column=1, row=15)

exitbtn = tk.Button(frame1, text="Exit", activebackground="red",
                    activeforeground="blue", command=close_window)
exitbtn_font = font.Font(size=15, weight='bold',
                         family='microsoft yahei ui light')
exitbtn['font'] = exitbtn_font
exitbtn.grid(pady=(10, 10), column=2, row=15)

clrbtn = tk.Button(frame1, text="Clear", activebackground="yellow",
                   activeforeground="blue", command=clear_contents)
clrbtn_font = font.Font(size=15, weight='bold',
                        family='microsoft yahei ui light')
clrbtn['font'] = clrbtn_font
clrbtn.grid(pady=(10, 10), column=5, row=15)

frame1.pack()
window.mainloop()
