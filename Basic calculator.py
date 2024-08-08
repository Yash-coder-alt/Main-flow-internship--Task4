from tkinter import *           ###Tkinter is standard python interface of GUI toolkit
from PIL import ImageTk, Image  ###PIL is pillow which is python imaging library

#Function to initialise the calculator
def init_calculator():
    sm=Tk()
    sm.title("Basic Calculator")

    # Path of ICO file
    sm.iconbitmap('E:\\python projects\\Calculator Photo-20240804T123302Z-001\\Calculator Photo\\Calc-icon.ico')
    sm.geometry("300x430")

    # Path of background file
    bg= ImageTk.PhotoImage(file="E:\\python projects\\Calculator Photo-20240804T123302Z-001\\Calculator Photo\\300x430_background.png")
    bg_label=Label(sm, image=bg)
    bg_label.place(x=0,y=0)

    #Entry Widget
    e= Entry(sm, width=35, borderwidth=10, font=("Times",10))
    e.grid(row=0, column=0, pady=20, padx=20, columnspan=3)

    #Loading Images
    images ={
        "1":ImageTk.PhotoImage(file="E:\\python projects\\Calculator Photo-20240804T123302Z-001\\Calculator Photo\\1.png"),
        "2":ImageTk.PhotoImage(file="E:\\python projects\\Calculator Photo-20240804T123302Z-001\\Calculator Photo\\2.png"),
        "3":ImageTk.PhotoImage(file="E:\\python projects\\Calculator Photo-20240804T123302Z-001\\Calculator Photo\\3.png"),
        "4":ImageTk.PhotoImage(file="E:\\python projects\\Calculator Photo-20240804T123302Z-001\\Calculator Photo\\4.png"),
        "5":ImageTk.PhotoImage(file="E:\\python projects\\Calculator Photo-20240804T123302Z-001\\Calculator Photo\\5.png"),
        "6":ImageTk.PhotoImage(file="E:\\python projects\\Calculator Photo-20240804T123302Z-001\\Calculator Photo\\6.png"),
        "7":ImageTk.PhotoImage(file="E:\\python projects\\Calculator Photo-20240804T123302Z-001\\Calculator Photo\\7.png"),
        "8":ImageTk.PhotoImage(file="E:\\python projects\\Calculator Photo-20240804T123302Z-001\\Calculator Photo\\8.png"),
        "9":ImageTk.PhotoImage(file="E:\\python projects\\Calculator Photo-20240804T123302Z-001\\Calculator Photo\\9.png"),
        "0":ImageTk.PhotoImage(file="E:\\python projects\\Calculator Photo-20240804T123302Z-001\\Calculator Photo\\10.png"),
        "+":ImageTk.PhotoImage(file="E:\\python projects\\Calculator Photo-20240804T123302Z-001\\Calculator Photo\\11.png"),
        "-":ImageTk.PhotoImage(file="E:\\python projects\\Calculator Photo-20240804T123302Z-001\\Calculator Photo\\12.png"),
        "*":ImageTk.PhotoImage(file="E:\\python projects\\Calculator Photo-20240804T123302Z-001\\Calculator Photo\\13.png"),
        "/":ImageTk.PhotoImage(file="E:\\python projects\\Calculator Photo-20240804T123302Z-001\\Calculator Photo\\14.png"),
        "=":ImageTk.PhotoImage(file="E:\\python projects\\Calculator Photo-20240804T123302Z-001\\Calculator Photo\\15.png"),
        "C":ImageTk.PhotoImage(file="E:\\python projects\\Calculator Photo-20240804T123302Z-001\\Calculator Photo\\16.png")
    }

    # Defining button function

    def button_click(number):
        current=e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))
    
    def button_add():
        first_number=e.get()
        global f_num
        global maths
        maths="addition"
        f_num=int(first_number)
        e.delete(0, END)

    def button_sub():
        first_number=e.get()
        global f_num
        global maths
        maths="subtraction"
        f_num=int(first_number)
        e.delete(0, END)

    def button_mult():
        first_number=e.get()
        global f_num
        global maths
        maths="multiplication"
        f_num=int(first_number)
        e.delete(0, END)

    def button_div():
        first_number=e.get()
        global f_num
        global maths
        maths="division"
        f_num=int(first_number)
        e.delete(0, END)

    def button_equal():
        second_number=e.get()
        e.delete(0, END)
        sec_num=int(second_number)

        if maths=="addition":
            e.insert(0, f_num + int(sec_num))

        if maths=="subtraction":
            e.insert(0, f_num - int(sec_num))

        if maths=="multiplication":
            e.insert(0, f_num * int(sec_num))

        if maths=="division":
            e.insert(0, f_num / int(sec_num)) 

    def button_clear():
        e.delete(0, END)

    # Defining buttons
    buttons={
        "1":(1, 0, lambda: button_click(1)),
        "2":(1, 1, lambda: button_click(2)),
        "3":(1, 2, lambda: button_click(3)),
        "4":(2, 0, lambda: button_click(4)),
        "5":(2, 1, lambda: button_click(5)),
        "6":(2, 2, lambda: button_click(6)),
        "7":(3, 0, lambda: button_click(7)),
        "8":(3, 1, lambda: button_click(8)),
        "9":(3, 2, lambda: button_click(9)),
        "0":(4, 1, lambda: button_click(0)),
        "+":(4, 2, button_add),
        "-":(4, 0, button_sub),
        "*":(5, 1, button_mult),
        "/":(5, 2, button_div),
        "=":(5, 0, button_equal),
        "C":(6, 1, button_clear)
    }

    for btn, (row, col, cmd) in buttons.items():
        Button(sm, border="3", image=images[btn], command=cmd).grid(row=row, column=col)

    #Reference to images
    sm.images = images

    sm.mainloop()

#Initialization of calculator

init_calculator()    