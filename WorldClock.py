from datetime import datetime
import pytz
from tkinter import *
import time

root = Tk()
root.geometry("315x175")

def times():
    home = pytz.timezone('Asia/Jerusalem')
    local_time = datetime.now(home)
    current_time = local_time.strftime("%x WW%U\n%X%p")
    clock.config(text=current_time)
    name.config(text = 'Israel')

    home = pytz.timezone('Europe/Dublin')
    local_time = datetime.now(home)
    current_time = local_time.strftime("%x WW%U\n%X%p")
    clock1.config(text=current_time)
    name1.config(text='Ireland')

    home = pytz.timezone('America/Phoenix')
    local_time = datetime.now(home)
    current_time = local_time.strftime("%x WW%U\n%X%p")
    clock2.config(text=current_time)
    name2.config(text='Phoenix[AZ]')

    home = pytz.timezone('US/Pacific')
    local_time = datetime.now(home)
    current_time = local_time.strftime("%x WW%U\n%X%p")
    clock3.config(text=current_time)
    name3.config(text='Portland[OR]')

    clock.after(200, times)


LabelSize = 15
ClockSize = 15

name = Label(root, font=("times",LabelSize,"bold"))
name.place(x=35, y=5)
clock=Label(root, font=("times",ClockSize,"bold"))
clock.place(x=10, y=30)

name1 = Label(root, font=("times",LabelSize,"bold"))
name1.place(x=185, y=5)
clock1=Label(root, font=("times",ClockSize,"bold"))
clock1.place(x=160, y=30)

name2 = Label(root, font=("times",LabelSize,"bold"))
name2.place(x=20, y=85)
clock2=Label(root, font=("times",ClockSize,"bold"))
clock2.place(x=10, y=110)

name3 = Label(root, font=("times",LabelSize,"bold"))
name3.place(x=185, y=85)
clock3=Label(root, font=("times",ClockSize,"bold"))
clock3.place(x=160, y=110)


times()

root.mainloop()


