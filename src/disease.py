from tkinter import *
import sqlite3
import tkinter.messagebox
import os.path
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from HospitalManagementDBMS import settings



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "../database.db")
conn = sqlite3.connect(db_path)
c = conn.cursor()

ids = []

class Application:
    def __init__(self, master):
        self.master = master

        self.frame = Frame(master, width=1200, height=720, bg='lightgreen')
        self.frame.pack(side=LEFT)


        self.heading = Label(self.frame, text="Add Reasons", font=('arial 40 bold'), fg='black', bg='lightgreen')
        self.heading.place(x=0, y=0)

        self.name = Label(self.frame, text="Name", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.name.place(x=0, y=100)

        self.cost = Label(self.frame, text="Cost", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.cost.place(x=0, y=140)

        self.name_ent = Entry(self.frame, width=30)
        self.name_ent.place(x=250, y=100)

        self.cost_ent = Entry(self.frame, width=30)
        self.cost_ent.place(x=250, y=140)

        self.submit = Button(self.frame, text="Add", width=20, height=2, bg='steelblue', command=self.add_reason)
        self.submit.place(x=200, y=200)

    def add_reason(self):
        self.val1 = self.name_ent.get()
        self.val2 = self.cost_ent.get()

        if self.val1 == '' or self.val2 == '':
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        else:
            sql = "INSERT INTO 'reason' (name, cost) VALUES(?, ?)"
            c.execute(sql, (self.val1, self.val2))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Reason added")
            self.name_ent.delete(0,'end')
            self.cost_ent.delete(0,'end')

root = Tk()
b = Application(root)
root.geometry("1200x720+0+0")
root.title("New Reason")
root.resizable(False, False)
root.mainloop()
            
