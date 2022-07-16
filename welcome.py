from tkinter import *
import admin
import student

def page():
    root = Tk()
    root.title("Welcome page")
    root.geometry("1350x3700+0+0")
    root.config(bg="ghost white")


    def staff():
        #print("admin")
        root.withdraw()
        admin.staff()

    def student():
        #print("Student")
        root.withdraw()
        student.student()

    #main page / first page (tkinter object window.)
    main = Frame(root, bg="black")
    main.pack()

    logo_lbl = Label(main, text="NUHU BAMMALI POLYTECHNIC", bg="green",
                    font=("Helvetica", 40, "bold"), width=30, height=4)
    logo_lbl.pack(side=TOP, pady=30)

    logo_lbl1 = Label(main, bd=2, text="Zaria, Kaduna State", width=30, font=(
        "Helvetica", 30, "bold"), padx=200, pady=10, bg="red")
    logo_lbl1.pack()

    # lblFrame = LabelFrame(main, bd=5, padx=200, pady=20, bg="ghost white", relief=RIDGE)
    # lblFrame.pack()

    admin_lbl = Button(main, text="Staff", bd=10, font=("Consolas", 40, "bold"), command=staff )
    admin_lbl.pack(pady=20)

    stud_lbl = Button(main, text="Student", bd=15, font=("Consolas", 40, "bold"), command=student)
    stud_lbl.pack(pady=20)

    root.mainloop()


#page()