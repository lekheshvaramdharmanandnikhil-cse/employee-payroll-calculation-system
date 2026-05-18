import tkinter
import pymysql
import datetime
from tkinter import*
import html
from tkinter import ttk
from tkinter import messagebox
def showadmintablesave():
    t=tkinter.Tk()
    t.geometry('1300x800')
    t.title('Save')
    
    d=Canvas(t,height=1500,width=1500,bg='red')
    d.place(x=0,y=0)
    head=Label(t,text='Admin Table Save',font=('arial',30,"italic underline"),fg='black',bg='silver')
    head.place(x=380,y=10)
    
    
    def filldata():
        db=pymysql.connect( host='localhost',user='root',password='root',database='epcs')
        cur=db.cursor()
        lt=[]
        sql="select adminid from admin"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
            e1['values']=lt
     
    
    def checkdata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='epcs')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select count(*) from admin where adminid=%d"%(xa)
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
        xb=e2.get()
        xc=e3.get()
        xd=e4.get()
        
        sql="insert into admin values('%d','%s','%s','%s')" %(xa,xb,xc,xd)
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
    
    
    a=Label(t,text='Admin-Id',font=('georgia',25,"italic underline"),fg='black',bg='silver')
    a.place(x=300,y=100)
    e1=Entry(t,width=20,bd=15)
    e1.place(x=500,y=100)
    
    
    b=Label(t,text='Name',font=('georgia',25,"italic underline"),fg='black',bg='silver')
    b.place(x=300,y=190)
    e2=Entry(t,width=20,bd=15)
    e2.place(x=500,y=190)
    
    c=Label(t,text='Password',font=('georgia',25,"italic underline"),fg='black',bg='silver')
    c.place(x=300,y=280)
    e3=Entry(t,width=20,bd=15)
    e3.place(x=500,y=280)
    
    d=Label(t,text='Email-Id',font=('georgia',25,"italic underline"),fg='black',bg='silver')
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