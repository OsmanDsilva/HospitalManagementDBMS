from tkinter import *
import sqlite3
import os.path
import datetime
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
        self.heading = Label(master, text="Sagar Hospitals",  fg='steelblue',bg='lightgreen', font=('arial 40 bold'))
        self.heading.place(x=150, y=0)
        now = datetime.datetime.now()
        date = now.strftime("%d-%m-%Y %H:%M")
        self.heading = Label(master, text=date, bg='lightgreen')
        self.heading.place(x=750, y=10)


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


        self.ent1 = Label(self.master, width=30, text=str(self.name1), bg='lightgreen', anchor=W, font=('arial 14'))
        self.ent1.place(x=300, y=140)


        self.ent4 = Label(self.master, width=30, text=str(self.location), bg='lightgreen', anchor=W, font=('arial 14'))
        self.ent4.place(x=300, y=180)

        self.ent5 = Label(self.master, width=30, text=str(self.phone), bg='lightgreen', anchor=W, font=('arial 14'))
        self.ent5.place(x=300, y=220)

        frameReason = Frame(self.master,bg='lightgreen',relief = 'sunken',borderwidth=2,width=420,height=200)
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

        condition = (settings.diseases[settings.diseases.index(self.reason)])
        comand1 = "SELECT * FROM reason where name LIKE ?"
        self.res = c.execute(comand1,(settings.diseases[settings.diseases.index(self.reason)],))
        for self.row in self.res :
            varCost = self.row[1]
            varMedCost = self.row[2]
        self.ent7 = Label(frameReason, text=condition, anchor=W,bg='lightgreen',font=('arial 14 bold'))
        self.ent7.place(x=300,y=0)

        self.ent8 = Label(frameReason, text=varCost, anchor=W,bg='lightgreen',font=('arial 14 bold'))
        self.ent8.place(x=300,y=40)

        gst = int(varCost*0.14)
        self.ent9 = Label(frameReason, text=gst, anchor=W,bg='lightgreen',font=('arial 14 bold'))
        self.ent9.place(x=300,y=80)

        self.ent10 = Label(frameReason, text=varMedCost, anchor=W,bg='lightgreen',font=('arial 14 bold'))
        self.ent10.place(x=300,y=120)

        self.ent11 = Label(frameReason, text=varCost+gst+varMedCost, anchor=W,bg='lightgreen',font=('arial 14 bold'))
        self.ent11.place(x=300,y=160)


        self.update = Button(self.master, text="Print", width=20, height=2, bg='lightblue')
        self.update.place(x=300, y=500)

        self.delete = Button(self.master, text="Save", width=20, height=2, bg='red')
        self.delete.place(x=0, y=500)
root = Tk()
b = Application(root)
root.geometry("1200x720+0+0")
root.title("Billing")
root.resizable(False, False)
root.config(bg='lightgreen')
root.mainloop()
