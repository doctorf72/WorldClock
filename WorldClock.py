from datetime import datetime
import pytz
#import tkinter as tk
from tkinter import *
import time

root = Tk()
root.geometry("325x175")
root.config(bg="black")


def times():

    home = pytz.timezone('Asia/Jerusalem')
    local_time = datetime.now(home)
    current_time = local_time.strftime("WW%U %x\n%a  %H:%M:%S")
    clock.config(text=current_time, bg="black", fg= "white")
    name.config(text = 'Israel', bg="black", fg= "white")

    home = pytz.timezone('Europe/Dublin')
    local_time = datetime.now(home)
    current_time = local_time.strftime("WW%U %x\n%a  %H:%M:%S")
    clock1.config(text=current_time, bg="black", fg= "white")
    name1.config(text='Ireland', bg="black", fg= "white")

    home = pytz.timezone('America/Phoenix')
    local_time = datetime.now(home)
    current_time = local_time.strftime("WW%U %x\n%a  %H:%M:%S")
    clock2.config(text=current_time, bg="black", fg= "white")
    name2.config(text='Phoenix[AZ]', bg="black", fg= "white")

    home = pytz.timezone('US/Pacific')
    local_time = datetime.now(home)
    current_time = local_time.strftime("WW%U %x\n%a  %H:%M:%S")
    clock3.config(text=current_time, bg="black", fg= "white")
    name3.config(text='Portland[OR]', bg="black", fg= "white")

    clock.after(200, times)


LabelSize = 15
ClockSize = 15
titleFontStyle = "bold italic underline"

name = Label(root, font=("times",LabelSize,titleFontStyle))
name.place(x=40, y=5)
clock=Label(root, font=("times",ClockSize,"bold"))
clock.place(x=10, y=30)

name1 = Label(root, font=("times",LabelSize,titleFontStyle))
name1.place(x=190, y=5)
clock1=Label(root, font=("times",ClockSize,"bold"))
clock1.place(x=165, y=30)

name2 = Label(root, font=("times",LabelSize,titleFontStyle))
name2.place(x=20, y=85)
clock2=Label(root, font=("times",ClockSize,"bold"))
clock2.place(x=10, y=110)

name3 = Label(root, font=("times",LabelSize,titleFontStyle))
name3.place(x=180, y=85)
clock3=Label(root, font=("times",ClockSize,"bold"))
clock3.place(x=165, y=110)


times()

root.title("Felix's World Clock")
root.mainloop()


