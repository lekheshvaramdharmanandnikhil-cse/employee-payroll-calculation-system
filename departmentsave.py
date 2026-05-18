import pymysql
from tkinter import messagebox
import tkinter
from tkinter import*
from tkinter import ttk
def departmentsave() :
    t = tkinter.Tk()
    t.geometry('1300x750')

    bg = Canvas(t, height=1500, width=1500, bg='red')
    bg.place(x=0, y=0)

    head = Label(t, text='Department Save',
                 font=('arial',25,"italic underline"),
                 fg='black', bg='silver')
    head.place(x=450, y=10)

    # ================= FUNCTIONS =================

    def filldata():
            db=pymysql.connect( host='localhost',user='root',password='root',database='epcs')
            cur=db.cursor()
            lt=[]
            sql="select deptid from department"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                lt.append(res[0])
                e1['values']=lt
    def checkdata():
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             database='epcs')
        cur = db.cursor()

        if len(e1.get()) == 0:
            messagebox.showerror("Error", "Select Department ID")
            return

        xa = int(e1.get())
        sql = "select count(*) from department where depid=%d" % xa
        cur.execute(sql)
        data = cur.fetchone()

        if data[0] == 0:
            mes.config(fg='Green', text='Allowed ! \n U Can Proceed')
        else:
            mes.config(fg='Black', text='Not Allowed !')

        db.close()

    def count():
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             database='epcs')
        cur = db.cursor()

        if len(e1.get()) == 0:
            messagebox.showerror("Error", "Select Department ID")
            return

        deptid = int(e1.get())
        sql = "select count(staffid) from staff where deptid=%d" % deptid
        cur.execute(sql)
        data = cur.fetchone()

        e6.delete(0, END)
        e6.insert(0, data[0])

        db.close()

    def savedata():
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             database='epcs')
        cur = db.cursor()

        if (len(e1.get())==0 or len(e2.get())==0 or
            len(e3.get())==0 or len(e4.get())==0 or
            len(e5.get())==0 or len(e6.get())==0):

            mes.config(fg='Green', text='Please Fill \n All Data :(')

        else:
            xa = int(e1.get())
            xb = e2.get()
            xc = e3.get()
            xd = e4.get()
            xe = e5.get()
            xf = int(e6.get())

            sql = """insert into department
            values(%d,'%s','%s','%s','%s',%d)""" % (
                xa, xb, xc, xd, xe, xf)

            cur.execute(sql)
            db.commit()

            mes.config(fg='dark red', text='Data Saved :)')

            e1.set('')
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)

        db.close()

    def close():
        t.destroy()

    # ================= MESSAGE =================

    mes = Label(t, text='', font=('arial',24),
                bg='red', width=40, height=3)
    mes.place(x=350, y=80)

    # ================= LABELS & ENTRIES =================

    a = Label(t, text='Dep-Id',
              font=('georgia',25,"italic underline"),
              bg='silver')
    a.place(x=320, y=160)

    e1 = ttk.Combobox(t, width=20)
    e1.place(x=550, y=160)
    filldata()

    b = Label(t, text='DName',
              font=('georgia',25,"italic underline"),
              bg='silver')
    b.place(x=310, y=240)
    e2 = Entry(t, width=20, bd=15)
    e2.place(x=550, y=240)

    c = Label(t, text='Hodname',
              font=('georgia',25,"italic underline"),
              bg='silver')
    c.place(x=280, y=320)
    e3 = Entry(t, width=20, bd=15)
    e3.place(x=550, y=320)

    d = Label(t, text='Hodemail-Id',
              font=('georgia',25,"italic underline"),
              bg='silver')
    d.place(x=235, y=400)
    e4 = Entry(t, width=20, bd=15)
    e4.place(x=550, y=400)

    e = Label(t, text='Special Remarks',
              font=('georgia',25,"italic underline"),
              bg='silver')
    e.place(x=180, y=480)
    e5 = Entry(t, width=20, bd=15)
    e5.place(x=550, y=480)

    f = Label(t, text='No-Of-Employee',
              font=('georgia',25,"italic underline"),
              bg='silver')
    f.place(x=180, y=560)
    e6 = Entry(t, width=20, bd=15)
    e6.place(x=550, y=560)

    # ================= BUTTONS =================

    b1 = Button(t, text='Save', command=savedata,
                font=('georgia',20,"italic underline"),
                bg='silver', width=10)
    b1.place(x=850, y=240)

    b2 = Button(t, text='Check', command=checkdata,
                font=('georgia',20,"italic underline"),
                bg='silver', width=10)
    b2.place(x=850, y=160)

    b3 = Button(t, text='Count', command=count,
                font=('georgia',20,"italic underline"),
                bg='silver', width=10)
    b3.place(x=850, y=320)

    b4 = Button(t, text='Close', command=close,
                font=('georgia',20,"italic underline"),
                bg='silver', width=10)
    b4.place(x=850, y=400)

    t.mainloop()