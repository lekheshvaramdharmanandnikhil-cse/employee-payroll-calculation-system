import tkinter
from tkinter import *
from operator import*
from operator import*
t = tkinter.Tk()
t.geometry('1300x800')
z = Canvas(t, width=1300, height=800, bg='#FFF6E5')
z.place(x=0, y=0)
z.create_line(23,530,462,530,width=6)
z.create_line(23,660,462,660,width=6)
z.create_line(25,530,25,660,width=6)
z.create_line(460,530,460,660,width=6)
z.create_line(296,18,965,18,width=6)
z.create_line(296,73,965,73,width=6)
z.create_line(299,18,299,73,width=6)
z.create_line(962,18,962,73,width=6)
x = Label(t,text=' Employee Payroll Calculation System ',bg='#009688',  fg='white',font=('garamond', 30, 'bold'))
x.place(x=300, y=20)
b1 = Button(t,text='GET STARTED',font=('garamond', 25, 'bold'),fg='white',bg='#009688',width=15, height=1,bd=10,command=showprojectplaytime)
b1.place(x=850, y=550)
a = Label(t,text='Welcome !',font=('garamond', 30, 'underline bold'),bg='#F9F9F9', fg='black')
a.place(x=15, y=130)
info_bg = '#FFFFFF'
info_fg = '#222222' 
for i, text in enumerate(['An Employee Payroll Calculation System is a software tool used to manage employee salary,',
'attendance, and deductions automatically.',
'It reduces manual work by calculating gross pay, net pay, bonuses, taxes,',
'and allowances accurately.',
'The system stores employee details such as name, ID, designation, salary structure,',
'and working days.']):
    lbl = Label(t,text=text,font=('garamond', 25, 'underline bold'),bg=info_bg,fg=info_fg)
    lbl.place(x=15, y=180 + i*40)
a8 = Label(t,text='TEAM MEMBERS NAME :',font=('garamond', 25, 'underline bold'),bg=info_bg, fg=info_fg)
a8.place(x=35, y=550)
a9 = Label(t, text='GUNMAY', font=('garamond', 25, 'bold'),bg=info_bg, fg=info_fg)
a9.place(x=60, y=600)
a10 = Label(t, text='ARCHIT', font=('garamond', 25, 'bold'),bg=info_bg, fg=info_fg)
a10.place(x=250, y=600)
t.mainloop()