from tkinter import *
import student
import welcome


def staff():
    root = Tk()
    root.title("Welcome page")
    root.geometry("1350x3700+0+0")
    root.config(bg="gray")

    def post():
        print("admin")

    def back():
        # print("Student")
        root.withdraw()
        welcome.page()

    username = StringVar()
    password = StringVar()
    # main page / first page (tkinter object window.)
    main = Frame(root, bg="yellow")
    main.pack()

    logo_lbl = Label(main, text="NUHU BAMMALI POLYTECHNIC", bg="red",
                     font=("Helvetica", 40, "bold"), width=30, height=2)
    logo_lbl.pack(side=TOP, pady=20)

    logo_lbl1 = Label(main, bd=2, text="Zaria, Kaduna State", width=30, font=(
        "Helvetica", 30, "bold"), padx=200, pady=10, bg="green")
    logo_lbl1.pack()

    username_lbl = Label(main, text="username", font=(
        "Arial", 25, "bold"), width=10, bg='yellow')
    username_lbl.pack(pady=20)

    username_entry = Entry(main, textvariable=username,
                           font=("consolas", 14), width=20)
    username_entry.pack()

    password_lbl = Label(main, text="password", font=(
        "Arial", 25, "bold"), width=10, bg='yellow')
    password_lbl.pack(pady=20)

    password_entry = Entry(main, textvariable=password,
                           font=("consolas", 14), width=20)
    password_entry.pack()

    admin_lbl = Button(main, text="Login", bd=5,
                       font=("Consolas", 20, "bold"), command=post)
    admin_lbl.pack(pady=20)

    stud_lbl = Button(main, text="Back", bd=5, font=(
        "Consolas", 20, "bold"), command=back)
    stud_lbl.pack(pady=20)

    # logo_lbl = Label(root, text="NUHU BAMMALI POLYTECHNIC", bg="green",
    #                 font=("Helvetica", 40, "bold"), width=30, height=4)
    # logo_lbl.grid(row=0, column=0)

    # logo_lbl1 = Label(root, bd=2, text="Zaria, Kaduna State", width=30, font=(
    #     "Helvetica", 30, "bold"), padx=200, pady=10, bg="red")
    # logo_lbl1.grid(row=1, column=0, pady=20)

    # admin_lbl = Button(root, text="Post Result", bd=10, font=("Consolas", 40, "bold"), command=post )
    # admin_lbl.grid(row=2, column=0)

    # stud_lbl = Button(root, text="Back", bd=15, font=("Consolas", 40, "bold"), command=back)
    # stud_lbl.grid(row=2, column=1)

    root.mainloop()


# staff()
