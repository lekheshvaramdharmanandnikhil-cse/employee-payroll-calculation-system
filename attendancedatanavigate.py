import tkinter
import pymysql
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
def attendancedatanavigate() :
    t=tkinter.Tk()
    t.geometry('1300x720')
    d=Canvas(t,height=1500,width=1500,bg='blue')
    d.place(x=0,y=0)
    head=Label(t,text='Attendance Data Navigate',font=('arial',30,"italic underline"),fg='black',bg='light blue')
    head.place(x=450,y=10)
    xa=[]
    xb=[]
    xc=[]
    xd=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='epcs')
        cur=db.cursor()
        sql="select * from attendancedata"
        cur.execute(sql)
        data=cur.fetchall()
        for r in data:
            xa.append(r[0])
            xb.append(r[1])
            xc.append(r[2])
            xd.append(r[3])
        db.close()
    def firstdata():
        global i
        i=0
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
    def nextdata():
        global i
        i=i+1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
    def prevdata():
        global i
        i=i-1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
    def lastdata():
        global i
        i=len(xa)-1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
    def close() :
        t.destroy()
    a=Label(t,text='Staff-Id',font=('georgia',25,"italic underline"),fg='black',bg='sky blue')
    a.place(x=300,y=100)
    e1=Entry(t,width=20,bd=15)
    e1.place(x=530,y=100)
    b=Label(t,text='Date-Of-Present',font=('georgia',25,"italic underline"),fg='black',bg='sky blue')
    b.place(x=250,y=190)
    e2=Entry(t,width=20,bd=15)
    e2.place(x=530,y=190)
    c=Label(t,text='Month',font=('georgia',25,"italic underline"),fg='black',bg='sky blue')
    c.place(x=300,y=280)
    e3=Entry(t,width=20,bd=15)
    e3.place(x=530,y=280)
    d=Label(t,text='Status',font=('georgia',25,"italic underline"),fg='black',bg='sky blue')
    d.place(x=300,y=370)
    e4=Entry(t,width=20,bd=15)
    e4.place(x=530,y=370)
    b1=Button(t,text='First',command=firstdata,font=('georgia',25,"italic underline"),fg='black',bg='sky blue',width=9)
    b1.place(x=750,y=95)
    b2=Button(t,text='Next',command=nextdata,font=('georgia',25,"italic underline"),fg='black',bg='sky blue',width=9)
    b2.place(x=750,y=205)
    b3=Button(t,text='Previous',command=prevdata,font=('georgia',25,"italic underline"),fg='black',bg='sky blue',width=9)
    b3.place(x=750,y=315)
    b4=Button(t,text='Last',command=lastdata,font=('georgia',25,"italic underline"),fg='black',bg='sky blue',width=9)
    b4.place(x=750,y=425)
    b5=Button(t,text='Close',command=close,font=('georgia',25,"italic underline"),fg='black',bg='sky blue',width=9)
    b5.place(x=750,y=535)
    filldata()
    t.mainloop()