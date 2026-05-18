import tkinter
import pymysql
import datetime
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def attendancedatasave() :
    t=tkinter.Tk()
    t.geometry('1300x800')
    t.title('Save')

    d=Canvas(t,height=1500,width=1500,bg='red')
    d.place(x=0,y=0)
    head=Label(t,text='Attendance Data Save',font=('arial',30,"italic underline"),fg='black',bg='silver')
    head.place(x=380,y=10)


    def filldata():
        db=pymysql.connect( host='localhost',user='root',password='root',database='epcs')
        cur=db.cursor()
        lt=[]
        sql="select staffid from attendancedata"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
            e1['values']=lt
    def showmonth():
        
        d=datetime.datetime.now()
        s=d.month
        if s==1:
            e3.insert(0,"jan")
        if s==2:
            e3.insert(0,"Feb")
        if s==3:
            e3.insert(0,"Mar")
        if s==4:
            e3.insert(0,"Apr")    
        if s==5:
            e3.insert(0,"May")
        if s==6:
            e3.insert(0,"jun")
        if s==7:
            e3.insert(0,"Jul")
        if s==8:
            e3.insert(0,"Aug") 
        if s==9:
            e3.insert(0,"Sept")
        if s==10:
            e3.insert(0,"Oct")
        if s==11:
            e3.insert(0,"Nov")
        if s==12:
            e3.insert(0,"Dec") 
 

    def checkdata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='epcs')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select count(*) from attendancedata where staffid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        if data[0]==0:
            mes.config(fg='Green')
            mes.config(text='Allowed ! \n U Can Proceed')
        else:
            mes.config(fg='Black')
            mes.config(text='Not Allowed !')
        db.close() 

    def savedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='epcs')
        cur=db.cursor()
        
        xa=int(e1.get())
        xb=int(e2.get())
        xc=e3.get()
        xd=int(e4.get())
        
        sql="insert into attendancedata values('%d','%d','%s','%d')" %(xa,xb,xc,xd)
        cur.execute(sql)    
        db.commit()
        mes.config(fg='dark red')
        mes.config(text='Data Saved :)') 
        db.close()
        e1.delete(0,100)    
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
    def close() :
        t.destroy()


    mes=Label(t,text='',font=('arial',64),bg='red',width=20,height=5)
    mes.place(x=440,y=60)


    a=Label(t,text='Staff-Id',font=('georgia',25,"italic underline"),fg='black',bg='silver')
    a.place(x=300,y=100)
    e1=Entry(t,width=20,bd=15)
    e1.place(x=500,y=100)


    b=Label(t,text='Present Date',font=('georgia',25,"italic underline"),fg='black',bg='silver')
    b.place(x=250,y=190)
    e2=Entry(t,width=20,bd=15)
    e2.place(x=500,y=190)

    c=Label(t,text='Month',font=('georgia',25,"italic underline"),fg='black',bg='silver')
    c.place(x=300,y=280)
    e3=Entry(t,width=20,bd=15)
    e3.place(x=500,y=280)
    showmonth()

    d=Label(t,text='Status',font=('georgia',25,"italic underline"),fg='black',bg='silver')
    d.place(x=300,y=370)
    e4=Entry(t,width=20,bd=15)
    e4.place(x=500,y=370)

    b1=Button(t,text='Save',command=savedata,font=('georgia',20,"italic underline"),fg='black',bg='silver',bd=10,width=10,height=1)
    b1.place(x=280,y=550)
    b2=Button(t,text='Check',command=checkdata,font=('georgia',20,"italic underline"),fg='black',bg='silver',bd=10,width=10,height=1)
    b2.place(x=700,y=100)
    b3=Button(t,text='Close',command=close,font=('georgia',20,"italic underline"),fg='black',bg='silver',bd=10,width=10,height=1)
    b3.place(x=720,y=550)
    t.mainloop()