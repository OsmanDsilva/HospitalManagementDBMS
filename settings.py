import sqlite3
import os

global diseases
diseases=[]

global genders
genders=['others', 'male', 'female']

global times1
times1=[]

global names
names=[]

def init():

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    sql = "SELECT name FROM reason"
    res = c.execute(sql)

    for name in res:
        diseases.append(name[0])

    sql = "SELECT scheduled_time FROM appointments"
    res1 = c.execute(sql)

    for t in res1:
        times1.append(t[0])

    sql = "SELECT name FROM appointments"
    res1 = c.execute(sql)

    for name in res1:
        names.append(t[0])

def getdiseases():
    return diseases
