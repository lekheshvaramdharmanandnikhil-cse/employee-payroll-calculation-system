import tkinter
import pymysql
from tkinter import*
from tkinter import ttk
def attendancedatafind() :
    t=tkinter.Tk()
    t.geometry('1300x750')
    d=Canvas(t,height=1500,width=1500,bg='yellow')
    d.place(x=0,y=0)
    head=Label(t,text='attendance Data Find',font=('arial',30,"italic underline"),fg='black',bg='light yellow')
    head.place(x=450,y=10)
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
    def findata() :
        db=pymysql.connect(host='localhost',user='root',password='root',database='epcs')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select date,month,status from attendancedata where staffid=%d" %(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,str(data[2]))
        db.close()
    def close() :
        t.destroy()
    a=Label(t,text='Staff-Id',font=('georgia',20,"italic underline"),fg='black',bg='light yellow')
    a.place(x=350,y=100)
    e1=ttk.Combobox(t) 
    filldata()
    e1.place(x=550,y=100)
    b1=Button(t,text='Find',font=('georgia',25,"italic underline"),fg='black',bg='light yellow',width=9,command=findata)
    b1.place(x=750,y=100)
    b=Label(t,text='Present Date',font=('georgia',20,"italic underline"),fg='black',bg='light yellow')
    b.place(x=350,y=190)
    e2=Entry(t,width=20,bd=15)
    e2.place(x=550,y=190)
    c=Label(t,text='Month',font=('georgia',20,"italic underline"),fg='black',bg='light yellow')
    c.place(x=350,y=280)
    e3=Entry(t,width=20,bd=15)
    e3.place(x=550,y=280)
    d=Label(t,text='Status',font=('georgia',20,"italic underline"),fg='black',bg='light yellow')
    d.place(x=350,y=370)
    e4=Entry(t,width=20,bd=15)
    e4.place(x=550,y=370)
    b2=Button(t,text='Close',font=('georgia',25,"italic underline"),fg='black',bg='light yellow',width=9,command=close)
    b2.place(x=750,y=350)
    t.mainloop()