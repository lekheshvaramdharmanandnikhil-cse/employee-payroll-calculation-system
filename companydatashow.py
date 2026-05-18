import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

import matplotlib
matplotlib.use("Agg")      # Stop matplotlib popup
import matplotlib.pyplot as plt

from PIL import Image, ImageTk


# ---------- GLOBAL IMAGE REFERENCE (VERY IMPORTANT) ----------
chart_img = None


def companydatashow():
    t = Tk()
    t.geometry('1100x800')
    t.title('Company Show')

    Canvas(t, width=1100, height=800, bg='sky blue').pack(fill='both', expand=True)

    Label(
        t,
        text='Company Show Data',
        font=('Arial Rounded MT Bold', 30, 'bold', 'italic'),
        bg='sky blue'
    ).place(x=300, y=10)

    e = Text(t, width=65, height=32, font=("verdana", 12, "bold"))
    e.place(x=10, y=80)

    # ---------- SHOW DATA ----------
    def filldata():
        e.delete("1.0", END)

        db = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='epcs'
        )
        cur = db.cursor()
        cur.execute("select * from companydata")
        data = cur.fetchall()
        db.close()

        msg = "ID\teName\tAddress\tPhone\tEmail\tRegNo\n"
        msg += "-" * 80 + "\n"

        for r in data:
            msg += f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\t{r[4]}\t{r[5]}\n"

        e.insert(END, msg)

    filldata()

    # ---------- SHOW SCATTER CHART ----------
    def showscatterchart():
        global chart_img

        db = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='epcs'
        )
        cur = db.cursor()
        cur.execute("select comid, regno from companydata")
        data = cur.fetchall()
        db.close()

        compid = []
        regno = []

        for r in data:
            compid.append(r[0])
            regno.append(r[1])

        plt.figure()
        plt.scatter(compid, regno)
        plt.xlabel("Company ID")
        plt.ylabel("Registration Number")
        plt.title("Company Scatter Chart")
        plt.tight_layout()
        plt.savefig("company_scatter.png")
        plt.close()

        img = Image.open("company_scatter.png")
        img = img.resize((380, 300))
        chart_img = ImageTk.PhotoImage(img)

        chart_lbl.config(image=chart_img)

    Button(
        t,
        text="Show Chart",
        font=("Arial", 12, "bold"),
        command=showscatterchart
    ).place(x=780, y=80)

    chart_lbl = Label(t, bg='sky blue')
    chart_lbl.place(x=700, y=130)

    t.mainloop()


# ---------- RUN FUNCTION ----------
companydatashow()
