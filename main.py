import sys
import os
import tkinter as tk

def run_appointment():
    os.system('python ./src/appointment.py')

def run_display():
    os.system('python ./src/display.py')

def run_update():
    os.system('python ./src/update.py')

top=tk.Tk()

top.geometry("500x300")
top.title("Sagar Hospital Appointments")
top.config(bg='steelblue')

b1=tk.Button(top,text="Add Appointments",width=20,height=2,command= run_appointment)
b2=tk.Button(top,text="Update Appointments",width=20,height=2,command= run_update)
b3=tk.Button(top,text="Display Appointments",width=20,height=2,command= run_display)

b1.pack()
b2.pack()
b3.pack()

top.mainloop()
