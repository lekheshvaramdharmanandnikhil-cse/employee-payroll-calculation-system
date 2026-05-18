import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def departmentshow() :
   t = tkinter.Tk()
   t.geometry("1600x1600")
   t.title("Department Show")

   Canvas(t, bg="light blue", width=1500, height=1500).place(x=0, y=0)

   Label(
       t,
       text="Department Show",
       font=("arial", 30, "italic underline"),
       bg="white"
   ).place(x=450, y=10)

   # ================= TEXT AREA =================
   txt = Text(t, width=95, height=20)
   txt.place(x=40, y=100)

   # ================= SHOW DEPARTMENT DATA =================
   def showdata():
       db = pymysql.connect(
           host="localhost",
           user="root",
           password="root",
           database="epcs"
       )
       cur = db.cursor()

       cur.execute("SELECT * FROM department")
       data = cur.fetchall()

       txt.delete(1.0, END)
       txt.insert(END, "ID\tName\tHOD\tEmail\tRemarks\tEmployees\n")
       txt.insert(END, "-" * 100 + "\n")

       for row in data:
           txt.insert(
               END,
               f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\n"
           )

       db.close()

   # ================= SHOW CHART =================
   def show_chart():
       db = pymysql.connect(
           host="localhost",
           user="root",
           password="root",
           database="epcs"
       )
       cur = db.cursor()

       # ---------- DEPARTMENT-WISE EMPLOYEES ----------
       cur.execute("""
           SELECT d.dname, COUNT(s.staffid)
           FROM department d
           LEFT JOIN staff s ON d.deptid = s.deptid
           GROUP BY d.dname
       """)
       dept_data = cur.fetchall()

       dept_names = [row[0] for row in dept_data if row[0] is not None]
       dept_counts = [row[1] for row in dept_data if row[0] is not None]

       # ---------- GENDER-WISE EMPLOYEES ----------
       cur.execute("""
           SELECT gender, COUNT(staffid)
           FROM staff
           WHERE gender IS NOT NULL
           GROUP BY gender
       """)
       gender_data = cur.fetchall()

       genders = [row[0] for row in gender_data]
       gender_counts = [row[1] for row in gender_data]

       db.close()

       # ---------- MATPLOTLIB FIGURE ----------
       fig = Figure(figsize=(3.5, 4))

       ax1 = fig.add_subplot(211)
       ax1.bar(dept_names, dept_counts)
       ax1.set_title("Employees Department-wise")
       ax1.set_ylabel("Employees")

       ax2 = fig.add_subplot(212)
       ax2.bar(genders, gender_counts)
       ax2.set_title("Male vs Female Employees")
       ax2.set_ylabel("Employees")

       fig.tight_layout()

       canvas = FigureCanvasTkAgg(fig, t)
       canvas.draw()
       canvas.get_tk_widget().place(x=820, y=100)

   # ================= BUTTONS =================
   Button(
       t, text="Show Data", command=showdata,
       font=("georgia", 18), width=12
   ).place(x=200, y=600)

   Button(
       t, text="Show Chart", command=show_chart,
       font=("georgia", 18), width=12
   ).place(x=400, y=600)

   Button(
       t, text="Close", command=t.destroy,
       font=("georgia", 18), width=12
   ).place(x=600, y=600)

   # ================= INITIAL LOAD =================
   showdata()
   t.mainloop()
