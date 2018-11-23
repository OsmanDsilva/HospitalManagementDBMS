import sys
import os
from tkinter import *
import settings

settings.init()

def run_appointment():
    os.system('python ./src/appointment.py')

def run_display():
    os.system('python ./src/display.py')

def run_update():
    os.system('python ./src/update.py')

def run_disease():
    os.system('python ./src/disease.py')

def run_billing():
    os.system('python ./src/billing.py')

top=Tk()

top.geometry("600x600")
top.title("Sagar Hospital")
top.config(bg='steelblue')

heading = Label(top, text="Sagar Hospital", font=('arial 35 bold'), fg='black', bg='steelblue')

b1=Button(top,text="Add Appointments",width=20,height=2,padx=3,pady=3,command= run_appointment)
b2=Button(top,text="Display Appointments",width=20,height=2,padx=3,pady=3,command= run_display)
b3=Button(top,text="Update Appointments",width=20,height=2,padx=3,pady=3,command= run_update)
b4=Button(top,text="Add Issues",width=20,height=2,padx=3,pady=3,command= run_disease)
b5=Button(top,text="Generate Bill",width=20,height=2,padx=3,pady=3,command= run_billing)

heading.pack(padx=10,pady=65)
b1.pack(padx=10,pady=10)
b2.pack(padx=10,pady=10)
b3.pack(padx=10,pady=10)
b4.pack(padx=10,pady=10)
b5.pack(padx=10,pady=10)

top.mainloop()
