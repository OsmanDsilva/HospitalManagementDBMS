from tkinter import *
import sqlite3
import tkinter.messagebox
import os.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "../database.db")
conn = sqlite3.connect(db_path)
c = conn.cursor()

ids = []

class Application:
    def __init__(self, master):
        self.master = master

        self.left = Frame(master, width=800, height=720, bg='lightgreen')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=400, height=720, bg='steelblue')
        self.right.pack(side=RIGHT)

        self.heading = Label(self.left, text="Sagar Hospital Appointments", font=('arial 40 bold'), fg='black', bg='lightgreen')
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

        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=250, y=100)

        self.age_ent = Entry(self.left, width=30)
        self.age_ent.place(x=250, y=140)

        self.gender_ent = Entry(self.left, width=30)
        self.gender_ent.place(x=250, y=180)

        self.location_ent = Entry(self.left, width=30)
        self.location_ent.place(x=250, y=220)

        self.phone_ent = Entry(self.left, width=30)
        self.phone_ent.place(x=250, y=260)
        
        self.time_ent = Entry(self.left, width=30)
        self.time_ent.place(x=250, y=300)

        self.submit = Button(self.left, text="Add Appointment", width=20, height=2, bg='steelblue', command=self.add_appointment)
        self.submit.place(x=300, y=340)

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
        self.val3 = self.gender_ent.get()
        self.val4 = self.location_ent.get()
        self.val6 = self.time_ent.get()
        self.val5 = self.phone_ent.get()

        self.name_ent.delete(0,'end')
        self.age_ent.delete(0,'end')
        self.gender_ent.delete(0,'end')
        self.location_ent.delete(0,'end')
        self.time_ent.delete(0,'end')
        self.phone_ent.delete(0,'end')


        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '':
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        else:
            sql = "INSERT INTO 'appointments' (name, age, gender, location,phone, scheduled_time) VALUES(?, ?, ?, ?, ?, ?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Appointment for " +str(self.val1) + " has been created" )

            self.box.insert(END, 'Appointment fixed for ' + str(self.val1) + ' at ' + str(self.val6) + '\n')

root = Tk()
b = Application(root)
root.geometry("1200x720+0+0")
root.title("New Apoointment")
root.resizable(False, False)
root.mainloop()
