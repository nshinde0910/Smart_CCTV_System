import tkinter as tk
import tkinter.font as font
from in_out import in_out
from motion import noise
from rect_noise import rect_noise
from record import record
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Smart cctv")
window.iconphoto(False, tk.PhotoImage(file='mn.png'))
window.geometry('900x650+300+50')
#window.eval('tk::PlaceWindow . center')


frame1 = tk.Frame(window)

label_title = tk.Label(frame1, text="Smart cctv Camera")
label_font = font.Font(size=35, weight='bold', family='Times New Roman')
label_title['font'] = label_font
label_title.grid(pady=(10, 10), column=2, row=1)


icon = Image.open('icons/spy.png')
icon = icon.resize((150, 150), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)
label_icon.grid(row=4, pady=(5, 10), column=2)

#btn1_image = Image.open('icons/lamp.png')
#btn1_image = btn1_image.resize((50, 50), Image.ANTIALIAS)
#btn1_image = ImageTk.PhotoImage(btn1_image)

btn2_image = Image.open('icons/rectangle-of-cutted-line-geometrical-shape.png')
btn2_image = btn2_image.resize((50, 50), Image.ANTIALIAS)
btn2_image = ImageTk.PhotoImage(btn2_image)

btn5_image = Image.open('icons/exit.png')
btn5_image = btn5_image.resize((50, 50), Image.ANTIALIAS)
btn5_image = ImageTk.PhotoImage(btn5_image)

btn3_image = Image.open('icons/security-camera.png')
btn3_image = btn3_image.resize((50, 50), Image.ANTIALIAS)
btn3_image = ImageTk.PhotoImage(btn3_image)

btn6_image = Image.open('icons/incognito.png')
btn6_image = btn6_image.resize((50, 50), Image.ANTIALIAS)
btn6_image = ImageTk.PhotoImage(btn6_image)

btn4_image = Image.open('icons/recording.png')
btn4_image = btn4_image.resize((50, 50), Image.ANTIALIAS)
btn4_image = ImageTk.PhotoImage(btn4_image)

# --------------- Button -------------------#
btn_font = font.Font(size=18, weight='bold', family='Helvetica')
# btn1 = tk.Button(frame1, text='Monitor', height=90, width=180,
#                 fg='green',  image=btn1_image, compound='left')
#btn1['font'] = btn_font
#btn1.grid(row=3, pady=(20, 10))

btn2 = tk.Button(frame1, text='Rectangle', height=90, width=180,
                 fg='orange', command=rect_noise, compound='left', image=btn2_image)
btn2['font'] = btn_font
btn2.grid(row=3, pady=(20, 10), column=3, padx=(20, 5))

btn_font = font.Font(size=20, weight='bold', family='microsoft yahei ui light')
btn3 = tk.Button(frame1, text='Monitor', height=90, width=180,
                 fg='green', command=noise, image=btn3_image, compound='left')
btn3['font'] = btn_font
btn3.grid(row=3, pady=(20, 10),  padx=(20, 5))

btn4 = tk.Button(frame1, text='Record', height=90, width=180,
                 fg='orange', command=record, image=btn4_image, compound='left')
btn4['font'] = btn_font
btn4.grid(row=5, pady=(20, 10), column=3)


btn6 = tk.Button(frame1, text='In Out', height=90, width=180,
                 fg='green', command=in_out, image=btn6_image, compound='left')
btn6['font'] = btn_font
btn6.grid(row=5, pady=(20, 10))

btn5 = tk.Button(frame1, height=90, width=180, fg='red',
                 command=window.quit, image=btn5_image)
btn5['font'] = btn_font
btn5.grid(row=6, pady=(20, 10), column=2)

frame1.pack()
window.mainloop()