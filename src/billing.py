from tkinter import *
import sqlite3
import os.path
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from HospitalManagementDBMS import settings

settings.init()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "../database.db")
conn = sqlite3.connect(db_path)
c = conn.cursor()

class Application:
    def __init__(self, master):
        self.master = master
        self.heading = Label(master, text="Billing",  fg='steelblue',bg='lightgreen', font=('arial 40 bold'))
        self.heading.place(x=150, y=0)

        self.name = Label(master, text="Enter Patient's Name",bg='lightgreen', font=('arial 18 bold'))
        self.name.place(x=0, y=60)

        self.namenet = Entry(master, width=30)
        self.namenet.place(x=280, y=62)

        self.search = Button(master, text="Search", width=12, height=1, bg='steelblue', command=self.search_db)
        self.search.place(x=350, y=102)

    def search_db(self):
        self.input = self.namenet.get()

        sql = "SELECT * FROM appointments WHERE name LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
                self.name1 = self.row[1]
                self.age = self.row[2]
                self.gender = self.row[3]
                self.location = self.row[4]
                self.time = self.row[6]
                self.phone = self.row[5]
                self.reason = self.row[7]

        self.uname = Label(self.master, text="Patient's Name",bg='lightgreen', font=('arial 18 bold'))
        self.uname.place(x=0, y=140)

        self.ulocation = Label(self.master, text="Location",bg='lightgreen', font=('arial 18 bold'))
        self.ulocation.place(x=0, y=180)

        self.uphone = Label(self.master, text="Phone Number",bg='lightgreen', font=('arial 18 bold'))
        self.uphone.place(x=0, y=220)


        self.ent1 = Label(self.master, width=30, text=str(self.name1), bg='lightgreen', anchor=W)
        self.ent1.place(x=300, y=140)


        self.ent4 = Label(self.master, width=30, text=str(self.location), bg='lightgreen', anchor=W)
        self.ent4.place(x=300, y=180)

        self.ent5 = Label(self.master, width=30, text=str(self.phone), bg='lightgreen', anchor=W)
        self.ent5.place(x=300, y=220)

        frameReason = Frame(self.master,bg='lightgreen',relief = 'sunken',borderwidth=2,width=400,height=200)
        frameReason.place(x=0, y=260)

        self.ureason = Label(frameReason, text="Reason", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.ureason.place(x=0, y=0)

        self.cost = Label(frameReason, text="Cost", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.cost.place(x=0, y=40)
        self.gst = Label(frameReason, text="GST", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.gst.place(x=0, y=80)
        self.meds = Label(frameReason, text="Cost of Medication", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.meds.place(x=0, y=120)
        self.total = Label(frameReason, text="Total", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.total.place(x=0, y=160)

        cCost = "SELECT cost from reason where name = ?"
        vCost = c.execute(cCost, (self.input,))
        self.ent7 = Label(frameReason, text=(settings.diseases[settings.diseases.index(self.reason)]), anchor=W,bg='lightgreen',font=('arial 14 bold'))
        self.ent7.place(x=300,y=0)



        # self.update = Button(self.master, text="Update", width=20, height=2, bg='lightblue')
        # self.update.place(x=400, y=420)
        #
        # self.delete = Button(self.master, text="Delete", width=20, height=2, bg='red')
        # self.delete.place(x=150, y=420)
root = Tk()
b = Application(root)
root.geometry("1200x720+0+0")
root.title("Billing")
root.resizable(False, False)
root.config(bg='lightgreen')
root.mainloop()
