import pymysql
from tkinter import*
import tkinter
from tkinter import ttk
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def staffsalarybreakupsave() :
    t=tkinter.Tk()
    t.geometry('1300x800')
    d=Canvas(t,height=1500,width=1500,bg='red')
    d.place(x=0,y=0)
    head=Label(t,text='Staff Salary Breakup Save',font=('arial',30,"italic underline"),fg='black',bg='silver')
    head.place(x=380,y=10)
    def calc():
        xa=int(e2.get())
        bs=round(xa*0.60)
        pf=round(bs*0.12)
        allowance=round(xa-(bs+pf))
        pm=round((bs+allowance)/12)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e3.insert(0, bs)
        e4.insert(0, pf)
        e5.insert(0,allowance)
        e6.insert(0, pm)
    def checkdata():
        db=pymysql.connect( host='localhost',user='root',password='root',database='epcs')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select count(*) from staffsalarybreakup where staffid=%d"%(xa)
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
        db=pymysql.connect( host='localhost',user='root',password='root',database='epcs')
        cur=db.cursor()
        xa=int(e1.get())
        xb=int(e2.get())
        xc=int(e3.get())
        xd=int(e4.get())
        xe=int(e5.get())
        xf=int(e6.get())
        sql="insert into staffsalarybreakup values(%d,%d,%d,%d,%d,%d)"%(xa,xb,xc,xd,xe,xf)
        cur.execute(sql)
        db.commit()
        mes.config(fg='dark red')
        mes.config(text='Data Saved :)') 
        db.close()
        t.config(bg='blue')
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
    def email() :
        from_address = "mandisjyoti@gmail.com"
        to_address = e7.get()
        
        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = 'Staff Salary Breakup'
        msg['From'] = from_address
        msg['To'] = to_address
        
        # Create the message (HTML).
        html = "Staff-Id\t:\t"+e1.get()+"<br>"+"CTC\t:\t"+e2.get()+"<br>"+"Basic\t:\t"+e3.get()+"<br>"+"PF\t:\t"+e4.get()+"<br>"+"Allowance\t:\t"+e5.get()+"<br>"+"Per Month\t:\t"+e6.get()
        
        # Record the MIME type - text/html.
        part1 = MIMEText(html, 'html')
        
        # Attach parts into message container
        msg.attach(part1)
        
        # Credentials
        username = 'mandisjyoti@gmail.com'  
        password = 'kdaqwacdpypbsnpq'
        
        # Sending the email
        ## note - this smtp config worked for me, I found it googling around, you may have to tweak the # (587) to get yours to work
        server = smtplib.SMTP('smtp.gmail.com', 587) 
        server.ehlo()
        server.starttls()
        server.login(username,password)  
        server.sendmail(from_address, to_address, msg.as_string())  
        server.quit()
        mes.config(fg='dark red')
        mes.config(text='Mail Sent :)') 
    def close() :
        t.destroy()
    mes=Label(t,text='',font=('arial',64),bg='red',width=20,height=5)
    mes.place(x=440,y=60)
    a=Label(t,text='Staff-Id',font=('georgia',25,"italic underline"),fg='black',bg='silver')
    a.place(x=300,y=100)
    e1=Entry(t,width=20,bd=15)
    e1.place(x=500,y=100)


    b=Label(t,text='CTC',font=('georgia',25,"italic underline"),fg='black',bg='silver')
    b.place(x=300,y=190)
    e2=Entry(t,width=20,bd=15)
    e2.place(x=500,y=190)

    c=Label(t,text='Basic',font=('georgia',25,"italic underline"),fg='black',bg='silver')
    c.place(x=300,y=280)
    e3=Entry(t,width=20,bd=15)
    e3.place(x=500,y=280)

    d=Label(t,text='PF',font=('georgia',25,"italic underline"),fg='black',bg='silver')
    d.place(x=300,y=370)
    e4=Entry(t,width=20,bd=15)
    e4.place(x=500,y=370)

    e=Label(t,text='Allowance',font=('georgia',25,"italic underline"),fg='black',bg='silver')
    e.place(x=300,y=460)
    e5=Entry(t,width=20,bd=15)
    e5.place(x=500,y=460)
    f=Label(t,text='Per-Month',font=('georgia',25,"italic underline"),fg='black',bg='silver')
    f.place(x=300,y=550)
    e6=Entry(t,width=20,bd=15)
    e6.place(x=500,y=550)
    g=Label(t,text='Email-Id',font=('georgia',25,"italic underline"),fg='black',bg='silver')
    g.place(x=300,y=640)
    e7=Entry(t,width=20,bd=15)
    e7.place(x=500,y=640)
    b1=Button(t,text='Save',command=savedata,font=('georgia',20,"italic underline"),fg='black',bg='silver',bd=10,width=10,height=1)
    b1.place(x=700,y=420)
    b2=Button(t,text='Check',command=checkdata,font=('georgia',20,"italic underline"),fg='black',bg='silver',bd=10,width=10,height=1)
    b2.place(x=700,y=100)
    b3=Button(t,text='Close',command=close,font=('georgia',20,"italic underline"),fg='black',bg='silver',bd=10,width=10,height=1)
    b3.place(x=700,y=620)
    b4=Button(t,text='Calculate',command=calc,font=('georgia',20,"italic underline"),fg='black',bg='silver',bd=10,width=10,height=1)
    b4.place(x=900,y=100)
    b5=Button(t,text='Send Email',command=email,font=('georgia',20,"italic underline"),fg='black',bg='silver',bd=10,width=10,height=1)
    b5.place(x=700,y=520)
    t.mainloop()