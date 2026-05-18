import pymysql
from tkinter import messagebox
import tkinter
from tkinter import*
from tkinter import ttk
def companydatasave() :
    t=tkinter.Tk()
    t.geometry('1300x750')
    d=Canvas(t,height=1500,width=1500,bg='red')
    d.place(x=0,y=0)
    head=Label(t,text='Company Data Save',font=('arial',25,"italic underline"),fg='black',bg='silver')
    head.place(x=450,y=10)
    def checkdata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='epcs')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select count(*) from companydata where compid=%d" %(xa)
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
        if len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 or len (e4.get())==0 or len (e5.get())==0 or len(e6.get())==0:
            mes.config(fg='Green')
            mes.config(text='Please Fill \n All Data :(')
        else:
            xa=int(e1.get())
            xb=e2.get()
            xc=e3.get()
            xd=e4.get()
            xe=e5.get()
            xf=int(e6.get())
            sql="insert into companydata values(%d,'%s','%s','%s','%s',%d)"%(xa,xb,xc,xd,xe,xf)
            cur.execute(sql)
            db.commit()
            mes.config(fg='dark red')
            mes.config(text='Data Saved :)')
            db.close()
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
    def close() :
        t.destroy()
    mes=Label(t,text='',font=('arial',64),bg='red',width=20,height=5)
    mes.place(x=440,y=100)
    a=Label(t,text='Comp-Id',font=('georgia',25,"italic underline"),fg='black',bg='silver')
    a.place(x=300,y=100)
    e1=Entry(t,width=20,bd=15)
    e1.place(x=500,y=100)

    
    b=Label(t,text='CName',font=('georgia',25,"italic underline"),fg='black',bg='silver')
    b.place(x=300,y=190)
    e2=Entry(t,width=20,bd=15)
    e2.place(x=500,y=190)
    
    c=Label(t,text='Address',font=('georgia',25,"italic underline"),fg='black',bg='silver')
    c.place(x=300,y=280)
    e3=Entry(t,width=20,bd=15)
    e3.place(x=500,y=280)
    
    d=Label(t,text='Phone',font=('georgia',25,"italic underline"),fg='black',bg='silver')
    d.place(x=300,y=370)
    e4=Entry(t,width=20,bd=15)
    e4.place(x=500,y=370)
    
    e=Label(t,text='Email-Id',font=('georgia',25,"italic underline"),fg='black',bg='silver')
    e.place(x=300,y=460)
    e5=Entry(t,width=20,bd=15)
    e5.place(x=500,y=460)
    f=Label(t,text='Reg-No',font=('georgia',25,"italic underline"),fg='black',bg='silver')
    f.place(x=300,y=550)
    e6=Entry(t,width=20,bd=15)
    e6.place(x=500,y=550)
    b1=Button(t,text='Save',command=savedata,font=('georgia',20,"italic underline"),fg='black',bg='silver',width=10,height=1)
    b1.place(x=700,y=544)
    b2=Button(t,text='Check',command=checkdata,font=('georgia',20,"italic underline"),fg='black',bg='silver',width=10,height=1)
    b2.place(x=700,y=100)
    b3=Button(t,text='Close',command=close,font=('georgia',20,"italic underline"),fg='black',bg='silver',width=10,height=1)
    b3.place(x=900,y=544)
    t.mainloop()