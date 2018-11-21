from tkinter import *
import sqlite3
import tkinter.messagebox
import os.path
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from HospitalManagementDBMS import settings

settings.init()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "../database.db")
conn = sqlite3.connect(db_path)
c = conn.cursor()

ids = []

class Application:
    def __init__(self, master):
        self.master = master

        self.left = Frame(master, width=700, height=720, bg='lightgreen')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=500, height=720, bg='steelblue')
        self.right.pack(side=RIGHT)

        self.heading = Label(self.left, text="Sagar Hospital Appointments", font=('arial 36 bold'), fg='black', bg='lightgreen')
        self.heading.place(x=0, y=0)

        self.name = Label(self.left, text="Patient's Name", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.name.place(x=0, y=100)

        self.age = Label(self.left, text="Age", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.age.place(x=0, y=140)

        self.gender = Label(self.left, text="Gender", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.gender.place(x=0, y=180)

        self.location = Label(self.left, text="Location", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.location.place(x=0, y=220)

        self.time = Label(self.left, text="Appointment Time", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.time.place(x=0, y=300)

        self.phone = Label(self.left, text="Phone Number", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.phone.place(x=0, y=260)

        self.reason = Label(self.left, text="Reason", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.reason.place(x=0, y=340)

        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=250, y=100)

        self.age_ent = Entry(self.left, width=30)
        self.age_ent.place(x=250, y=140)

        self.variable1 = StringVar(master)
        self.variable1.set(settings.genders[0])
        self.gender_ent = OptionMenu(master, self.variable1,*settings.genders)
        self.gender_ent.place(x=250, y=180)

        self.location_ent = Entry(self.left, width=30)
        self.location_ent.place(x=250, y=220)

        self.phone_ent = Entry(self.left, width=30)
        self.phone_ent.place(x=250, y=260)

        self.time_ent = Entry(self.left, width=30)
        self.time_ent.place(x=250, y=300)

        self.variable = StringVar(master)
        self.variable.set(settings.diseases[0])
        self.reason_ent = OptionMenu(master, self.variable,*settings.diseases)
        self.reason_ent.place(x=250, y=340)

        self.submit = Button(self.left, text="Add Appointment", width=20, height=2, bg='steelblue', command=self.add_appointment)
        self.submit.place(x=300, y=380)

        #getting the number of appointments fixed to view in the log
        sql2 = "SELECT ID FROM appointments"
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)

        self.new = sorted(ids)
        if(len(ids)==0):
            self.final_id=0;
        else:
            self.final_id = len(ids)

        self.logs = Label(self.right, text="Logs", font=('arial 28 bold'), fg='white', bg='steelblue')
        self.logs.place(x=0, y=0)

        self.box = Text(self.right, width=50, height=40)
        self.box.place(x=20, y=60)
        self.box.insert(END, "Total Appointments till now :  " + str(self.final_id) + '\n')

    def add_appointment(self):
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.variable1.get()
        self.val4 = self.location_ent.get()
        self.val6 = self.time_ent.get()
        self.val5 = self.phone_ent.get()
        self.val7 = self.variable.get()

        if self.val1 == '' or self.val2 == '' or self.val4 == '' or self.val5 == '' or self.val6 == '':
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        elif int(self.val2)<0 or int(self.val2)>150 or not self.val4.isalpha() or not self.val5.isdigit():
            tkinter.messagebox.showinfo("Warning", "Invalid input")
        elif self.val6 in settings.times1:
            tkinter.messagebox.showinfo("Warning", "Appointment at this time alreadry exits\n")
        else:
            sql = "INSERT INTO 'appointments' (name, age, gender, location,phone, scheduled_time, for) VALUES(?, ?, ?, ?, ?, ?, ?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6, self.val7))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Appointment for " +str(self.val1) + " has been created" )

            self.box.insert(END, 'Appointment fixed for ' + str(self.val1) + ' at ' + str(self.val6) + ' for ' + str(self.val7) + '\n')

            settings.times1.append(self.val6)
            self.name_ent.delete(0,'end')
            self.age_ent.delete(0,'end')
            self.location_ent.delete(0,'end')
            self.time_ent.delete(0,'end')
            self.phone_ent.delete(0,'end')

root = Tk()
b = Application(root)
root.geometry("1200x720+0+0")
root.title("New Apoointment")
root.resizable(False, False)
root.mainloop()
