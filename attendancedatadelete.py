import tkinter
import pymysql
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
def attendancedatadelete() :
    t=tkinter.Tk()
    t.geometry('1300x750')
    d=Canvas(t,height=1500,width=1500,bg='violet')
    d.place(x=0,y=0)
    head=Label(t,text='Attendance Data Delete',font=('arial',30,"italic underline"),fg='black',bg='white')
    head.place(x=400,y=10)
    def filldata() :
        db=pymysql.connect(host='localhost',user='root',password='root',database='epcs')
        cur=db.cursor()
        lt=[]
        sql="select staffid from attendancedata"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        e1['values']=lt
    def deldata() :
        db=pymysql.connect(host='localhost',user='root',password='root',database='epcs')
        cur=db.cursor()
        xa=int(e1.get())
        sql="delete from attendancedata where staffid=%d" %(xa)
        cur.execute(sql)
        db.commit()
        mes.config(fg='dark red')
        mes.config(text='Data Deleted :)')
        db.close()
        e1.delete(0,100)
    def close() :
        t.destroy()
    mes=Label(t,text='',font=('arial',64),bg='violet',width=20,height=5)
    mes.place(x=150,y=270)
    a=Label(t,text='Staff-Id',font=('georgia',30,"italic underline"),bg='light pink',height=1,width=7)
    a.place(x=400,y=160)
    e1=ttk.Combobox(t) 
    filldata()
    e1.place(x=650,y=160,height=50,width=150)
    c=Button(t,text='Delete',font=('georgia',30,"italic underline"),bg='light pink',height=1,width=7,command=deldata)
    c.place(x=680,y=280)
    c=Button(t,text='Close',font=('georgia',30,"italic underline"),bg='light pink',height=1,width=7,command=close)
    c.place(x=380,y=280)
    t.mainloop()