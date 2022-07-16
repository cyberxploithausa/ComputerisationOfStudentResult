from tkinter import *
import welcome
import os
import sys


root = Tk()
root.title("Login form")
root.geometry("1350x3700+0+0")
root.config(bg="black")


#button functions
#when clicked go to next page (admin or student)
def click():
    #withdrawing the window (Login form)
    root.withdraw()
    # print(root.wm_state())
    # if root.wm_state() == 'withdrawn':  # <----
    #     root.iconify()
    welcome.page()
    

#main page / first page (tkinter object window.)
main = Frame(root, bg="green")
main.pack()

logo_lbl = Label(main, text="NUHU BAMMALI POLYTECHNIC",
                font=("Helvetica", 40, "bold"))
logo_lbl.pack(side=TOP, pady=30)

logo_lbl1 = Label(main, bd=2, text="Zaria, Kaduna State", font=(
    "Helvetica", 30, "bold"), padx=200, pady=10, bg="red")
logo_lbl1.pack()

lblFrame = LabelFrame(main, bd=5, padx=200, pady=20, bg="ghost white", relief=RIDGE)
lblFrame.pack()

button = Button(lblFrame, text="CLICK TO CONTINUE >>>", fg="red", font=("Arial", 40, "bold"), command=click)
button.pack(side=BOTTOM, pady=30)


if __name__ == "__main__":
    #calling tkinter object
    #running the code
    root.mainloop()
