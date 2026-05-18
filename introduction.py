import tkinter
from tkinter import *
from projectplaytime import *
from projectplaytime import*
t = tkinter.Tk()
t.title('Employee Payroll Calculation System')
t.geometry('1300x800')
z = Canvas(t, width=1500, height=800, bg='#0F172A')
z.place(x=0, y=0)
x = Label(t,text=' Employee Payroll Calculation System ',bg='#0F172A',  fg='#38BDF8',font
          =('garamond', 30, 'underline bold'))
x.place(x=350, y=20)
b1 = Button(t,text='GET STARTED',font=('garamond', 20, 'bold'),fg='white',bg='#009688',width=15, height=1,bd=10,command=lambda: [t.destroy(),showprojectplaytime()])
b1.place(x=850, y=550)
a = Label(t,text='Welcome to My Employee Payroll Calculation System',font=('garamond', 20, 'underline bold'),bg='#0F172A', fg='#38BDF8')
a.place(x=370, y=270)
info_bg = '#FFFFFF'
info_fg = '#222222'
for i, text in enumerate(["Project Title: Employee Payroll Calculation System.",
    "This project demonstrates a GUI-based application developed using Python Tkinter.",
"The system is designed to calculate employee salaries based on attendance, allowances, and deductions.",
"It focuses on accuracy, simplicity, and ease of use for payroll management."]): 
    lbl = Label(t,text=text,font=('garamond', 15, 'bold'),bg='#0F172A',fg='white')
    lbl.place(x=15, y=350 + i*40)
a8 = Label(t,text='Developed by Python & Tkinter',font=('garamond', 15, 'underline bold'),bg='#0F172A', fg='white')
a8.place(x=15, y=550)
a9 = Label(t, text='Name: GUNMAY', font=('garamond', 25, 'bold'),bg='#0F172A', fg='white')
a9.place(x=520, y=130)
a10 = Label(t, text='Institue: E_GAIN', font=('garamond', 25, 'bold'),bg='#0F172A', fg='white')
a10.place(x=520, y=200)
t.mainloop()