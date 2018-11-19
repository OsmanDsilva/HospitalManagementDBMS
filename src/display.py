import tkinter as tk
import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "../database.db")
conn = sqlite3.connect(db_path)
c = conn.cursor()

sql = "SELECT * FROM appointments"
res = c.execute(sql)

root = tk.Tk()
root.title("Appointments")
root.geometry("400x300")
root.config(bg='lightgreen')

labels=["ID","  NAME"," AGE","  GENDER","   LOCATION"," PHONE NUMBER"," TIME"]

r=0
c=0

for l in labels:
    tk.Label(root, bg='lightgreen',text=l,borderwidth=1).grid(row=r,column=c)
    c=c+1
r=r+1

for i in res:
    for c in range(7):
        tk.Label(root, bg='lightgreen',text=i[c],borderwidth=1).grid(row=r,column=c)
        c=c+1
    r=r+1

root.mainloop()
