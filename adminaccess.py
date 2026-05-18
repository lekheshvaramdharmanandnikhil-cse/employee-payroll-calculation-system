import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random


t = tkinter.Tk()
t.geometry('500x400')
t.title('Admin Login')

generated_otp = None
otp_verified = False   # NEW (status flag)


def exit():
    t.destroy()
    

def login():
    loginid = e1.get()
    password = e2.get()
    email_id = e3.get()
    otp = e4.get()

    # 🔒 EMPTY FIELD CHECK
    if not loginid or not password or not email_id:
        messagebox.showerror("Error", "Please fill all fields")
        return

    # 🔒 ADMIN CREDENTIAL CHECK
    if loginid != "admin" or password != "1234":
        messagebox.showerror("Login Failed", "Invalid username or password")
        return

    # 🔒 OTP NOT FILLED
    if not otp:
        messagebox.showwarning("OTP Required", "Please fill OTP first")
        return

    # 🔒 OTP NOT VERIFIED
    if not otp_verified:
        messagebox.showwarning("OTP", "Please verify OTP first")
        return

    # ✅ ALL CONDITIONS PASSED
    messagebox.showinfo("Success", "Login Successful")
    t.destroy()


def verify():
    global generated_otp, otp_verified
    entered_otp = e4.get()

    if generated_otp is None:
        messagebox.showwarning("OTP", "Please send OTP first")
        return

    if not entered_otp:
        messagebox.showwarning("OTP", "Please enter OTP")
        return

    if entered_otp == generated_otp:
        otp_verified = True
        messagebox.showinfo("Success", "OTP Verified Successfully")
    else:
        otp_verified = False
        messagebox.showerror("Error", "Invalid OTP")


def email():
    from_address = "mandisjyoti@gmail.com"
    to_address = e3.get()

    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Admin OTP'
    msg['From'] = from_address
    msg['To'] = to_address

    html = (
        "Admin ID : " + e1.get() + "<br>" +
        "OTP : " + generated_otp
    )

    part1 = MIMEText(html, 'html')
    msg.attach(part1)

    username = 'mandisjyoti@gmail.com'
    password = 'kdaqwacdpypbsnpq'

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(username, password)
    server.sendmail(from_address, to_address, msg.as_string())
    server.quit()


def send_otp():
    global generated_otp, otp_verified
    otp_verified = False
    generated_otp = str(random.randint(100000, 999999))
    e4.delete(0, END)
    email()


# ================= UI =================

z = Canvas(t, width=1500, height=800, highlightthickness=0, bg='#0F172A')
z.place(x=0, y=0)

box_bg = Canvas(t, width=525, height=270, bg='#0F172A')
box_bg.place(x=45, y=90)

Label(t, text='Adminid:', font=('garamond', 12, 'bold'), bg='#0F172A', fg='white').place(x=70, y=120)
e1 = Entry(t, width=25, font=('garamond',12))
e1.place(x=170, y=122)

Label(t, text='Password:', font=('garamond', 12, 'bold'), bg='#0F172A', fg='white').place(x=70, y=170)
e2 = Entry(t, width=25, font=('garamond',12), show='*')
e2.place(x=170, y=172)

Label(t, text='Email ID:', font=('garamond', 12, 'bold'), bg='#0F172A', fg='white').place(x=70, y=220)
e3 = Entry(t, width=25, font=('garamond',12))
e3.place(x=170, y=222)

Label(t, text='OTP:', font=('garamond', 12, 'bold'), bg='#0F172A', fg='white').place(x=70, y=270)
e4 = Entry(t, width=25, font=('garamond',12))
e4.place(x=170, y=272)

Button(t, text='Login', width=12, bd=10, bg='light grey',
       font=('garamond', 10, 'bold'), command=login).place(x=60, y=300)

Button(t, text='Verify', width=12, bd=10, bg='light grey',
       font=('garamond', 10, 'bold'), command=verify).place(x=185, y=300)

Button(t, text='Close', width=12, bd=10, bg='light grey',
       font=('garamond', 10, 'bold'), command=exit).place(x=310, y=300)

Button(t, text='Send OTP', width=12, bd=10, bg='light grey',
       font=('garamond', 10, 'bold'), command=send_otp).place(x=435, y=300)

t.mainloop()
