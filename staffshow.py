import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
def staffshow() :
    t=tkinter.Tk()
    t.geometry('1300x750')
    d=Canvas(t,height=1500,width=1500,bg='light blue')
    d.place(x=0,y=0)
    head=Label(t,text='Staff Show',font=('arial',30,"italic underline"),fg='black',bg='white')
    head.place(x=450,y=10)
    def showdata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='epcs')
        cur=db.cursor()
        sql="select * from staff"
        msg="\n"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            msg=msg+str(res[0])+"\t"
            msg=msg+res[1]+"\t"
            msg=msg+res[2]+"\t"
            msg=msg+str(res[3])+"\t"
            msg=msg+res[4]+"\n"
        db.close()
        e.insert(END,msg)
    def close() :
        t.destroy()
    e=Text(t,width=100,height=25)
    showdata()
    e.place(x=250,y=100)
    b=Button(t,text='Close',command=close,font=('georgia',30,"italic underline"),fg='black',bg='white',width=10,height=1)
    b.place(x=500,y=550)
    t.mainloop()