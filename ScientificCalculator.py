#    -------->               My Project   (Scientific Calculator...)         <----------      #

import tkinter as tk
from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox
import math as m
import sqlite3
root = Tk()
root.configure(bg='#150019')
root.title('Scientific Calculator')
root.minsize(width=702, height=500)
root.maxsize(width=850, height=609)

#    --------->             Various Window_Functions that were described in the program           <---------  #

one = ''
two = ''
operation = ''
three= ''


def history_table():
    conn = sqlite3.connect('history.db')
    c = conn.cursor()
    delete_table()
    c.execute("""CREATE TABLE history1 (first_name text)""")
    conn.commit()
    conn.close()
def  delete_table():
    conn = sqlite3.connect('history.db')
    c = conn.cursor()
    c.execute("DROP TABLE history1")
    conn.commit()
    conn.close()

def  insert_table(three):
    conn =sqlite3.connect('history.db')
    c=conn.cursor()
    c.execute("INSERT INTO history1 VALUES (?)",(three,))

    conn.commit()
    conn.close()
def select_table():
    conn = sqlite3.connect('history.db')
    c=conn.cursor()
    c.execute("SELECT * FROM history1")
    print( c.fetchall())
    conn.commit()
    conn.close()

history_table()


def hide_layouts():
    entry_frame.grid_forget()
    frame_a.grid_forget()
    frame_b.grid_forget()


def Close():
    response = messagebox.askyesno("This is my PopUp..!", "Do You want to close Appliction...!")
    if (response == 1):
        delete_table()
        root.quit()
    else:
        pass


def layout_one():
    hide_layouts()
    entry_frame.grid(padx=20, pady=10)
    frame_a.grid()
    obj = layout_one(frame_a)


def layout_two():
    hide_layouts()
    entry_frame.grid(padx=20, pady=10)
    frame_b.grid(padx=30, pady=20)
    obj = layout_two(frame_b)


def color_picker():
    color = colorchooser.askcolor()[1]
    root.configure(bg=color)
    frame_a.configure(bg=color)
    frame_b.configure(bg=color)


#       -------->           Various kinds of Layout_Functions....(Buttons)               <-------------  #

def Clear_Last():
    temp = entry.get()
    if temp == '':
        messagebox.showwarning("End Clear Function", "Entry Widget is Empty..!")
    s = str(entry.get())
    length = len(s)
    entry.delete(length - 1)


def Clear():
    temp = entry.get()
    if temp == '':
        messagebox.showwarning("About Clear Function", "Entry Widget is Empty..!")
    entry.delete(0, END)


def Insert_Number(a):
    entry.insert(END, a)


def Insert_Pi():
    entry.insert(0, '3')


def Calculate_Operands():  # Calculates the first and second operands from the string...
    pointer = -1
    global one
    global two
    for i in one:
        if (i == '+' or i == '-' or i == '*' or i == '/' or i == '%' or i == '^'):
            pointer = pointer + 1
            break
        else:
            pointer = pointer + 1
    two = one[pointer + 1:]
    return (one[:pointer])


def Addition():
    global one
    global two
    global operation
    operation = 'addition'
    temp = entry.get()
    if temp == '':
        messagebox.showwarning('Warning', 'Please Enter a Number to perform Operation...')
    else:
        entry.insert(END, '+')


def Subraction():
    global one
    global two
    global operation
    operation = 'subraction'
    temp = entry.get()
    if temp == '':
        messagebox.showwarning('Warning', 'Please Enter a Number to perform Operation...')
    else:
        entry.insert(END, '-')


def Multiplication():
    global one
    global two
    global operation
    operation = 'multiplication'
    temp = entry.get()
    if temp == '':
        messagebox.showwarning('Warning', 'Please Enter a Number to perform Operation...')
    else:
        entry.insert(END, '*')


def Division():
    global one
    global two
    global operation
    operation = 'division'
    temp = entry.get()
    if temp == '':
        messagebox.showwarning('Warning', 'Please Enter a Number to perform Operation...')
    else:
        entry.insert(END, '/')


def ModularDivision():
    global one
    global two
    global operation
    operation = 'modulardivision'
    temp = entry.get()
    if temp == '':
        messagebox.showwarning('Warning', 'Please Enter a Number to perform Operation...')
    else:
        entry.insert(END, '%')


def Y_power_X():
    global one
    global two
    global operation
    operation = 'y_power_x'
    temp = entry.get()
    if temp == '':
        messagebox.showwarning('Warning', 'Please Enter a Number to perform Operation...')
    else:
        entry.insert(END, '^')


def Exp():
    a = entry.get()
    if a == '':
        messagebox.showwarning('Warning', 'Please Enter a Number to perform Operation...')
    else:
        entry.insert(0, m.exp(float(a)))


def X_Square():
    a = entry.get()
    if a == '':
        messagebox.showwarning('Warning', 'Please Enter a Number to perform Operation...')
    else:
        entry.delete(0, END)
        entry.insert(0, f" Square of {a} : {int(a) * int(a)}")


def X_Cube():
    a = entry.get()
    if a == '':
        messagebox.showwarning('Warning', 'Please Enter a Number to perform Operation...')
    else:
        entry.delete(0, END)
        entry.insert(0, f" Cube of {a} :{int(a) * int(a) * int(a)}")


def Square_Root():
    a = entry.get()
    if a == '':
        messagebox.showwarning('Warning', 'Please Enter a Number to perform Operation...')
    else:
        entry.delete(0, END)
        entry.insert(0, f" Square root of {a} is : {m.floor(m.sqrt(float(a)))}")


def Log_10():
    a = entry.get()
    if a == '':
        messagebox.showwarning('Warning', 'Please Enter a Number to perform Operation...')
    else:
        entry.delete(0, END)
        entry.insert(0, (f" Log({a}) is: {m.log10(float(a))}"))


def Factorial():
    a = entry.get()
    if a == '':
        messagebox.showwarning('Warning', 'Please Enter a Number to perform Operation...')
    else:
        entry.delete(0, END)
        entry.insert(0, f" {a}! = {m.factorial(float(a))}")


def Sine():
    a = entry.get()
    if a == '':
        messagebox.showwarning('Warning', 'Please Enter a Number to perform Operation...')
    else:
        entry.delete(0, END)
        entry.insert(0, f" Sin({a}) = {m.sin(float(a))}")


def Cosine():
    a = entry.get()
    if a == '':
        messagebox.showwarning('Warning', 'Please Enter a Number to perform Operation...')
    else:
        entry.delete(0, END)
        entry.insert(0, f" Cos({a}) = {m.cos(float(a))}")


def Tan():
    a = entry.get()
    if a == '':
        messagebox.showwarning('Warning', 'Please Enter a Number to perform Operation...')
    else:
        entry.delete(0, END)
        entry.insert(0, f" Tan({a}) = {m.tan(float(a))}")


def SineH():
    a = entry.get()
    if a == '':
        messagebox.showwarning('Warning', 'Please Enter a Number to perform Operation...')
    else:
        entry.delete(0, END)
        entry.insert(0, f" Sinh({a}) = {m.sinh(float(a))}")


def CosineH():
    a = entry.get()
    if a == '':
        messagebox.showwarning('Warning', 'Please Enter a Number to perform Operation...')
    else:
        entry.delete(0, END)
        entry.insert(0, f" Cosh({a}) = {m.cosh(float(a))}")


def TanH():
    a = entry.get()
    if a == '':
        messagebox.showwarning('Warning', 'Please Enter a Number to perform Operation...')
    else:
        entry.delete(0, END)
        entry.insert(0, f" Tanh({a}) = {m.tanh(float(a))}")


def is_Equal():
    global one
    global two
    global three
    global operation
    one = entry.get()
    three=entry.get()

    insert_table(str(three))
    if operation == 'addition':
        one = Calculate_Operands()
        entry.delete(0, END)
        entry.insert(0, int(one) + int(two))

    elif operation == 'subraction':
        one = Calculate_Operands()
        entry.delete(0, END)
        entry.insert(0, int(one) - int(two))

    elif operation == 'multiplication':
        one = Calculate_Operands()
        entry.delete(0, END)
        entry.insert(0, int(one) * int(two))

    elif operation == 'division':
        one = Calculate_Operands()
        entry.delete(0, END)
        entry.insert(0, int(one) / int(two))

    elif operation == 'modulardivision':
        one = Calculate_Operands()
        entry.delete(0, END)
        entry.insert(0, int(one) % int(two))

    elif operation == 'y_power_x':
        one = Calculate_Operands()
        entry.delete(0, END)
        entry.insert(0, int(m.pow(int(one), int(two))))


#    ---------->             Creating  a  Menu _ Bar  to hold down the Menu _ Items...        <------------     #

menu_bar = Menu(root)
root.config(menu=menu_bar)

menu1 = Menu(menu_bar)
menu_bar.add_cascade(label='Select_Layout', menu=menu1)

menu1.add_command(label='Basic_Calculator', command=layout_one)
menu1.add_command(label='Scientific_Calculator', command=layout_two)

menu2 = Menu(menu_bar)
menu_bar.add_cascade(label='Color_Changer', menu=menu2)
menu2.add_command(label='pick_a_color', command=color_picker)

menu3 = Menu(menu_bar)
menu_bar.add_cascade(label='CloseApplication', menu=menu3)
menu3.add_command(label='Close_Window', command=Close)

menu4 =Menu(menu_bar)
menu_bar.add_cascade(label='History',menu=menu4)
menu4.add_command(label='History' , command=select_table)

#   ------->   Two Different classes one for Simple_Layout of calculator  +  second class is for Layout with Scientific Functions as well     <------  #

class layout_one():
    def __init__(self, master):
        btn0 = tk.Button(master, text="0", bg="#7e06d4", fg="yellow", font=('Helvetica', 20, 'bold'), border=10,
                         width=2, height=1, command=lambda: Insert_Number('0'))
        btn0.grid(row=0, column=0, padx=15, pady=10)
        btn_Arrow = tk.Button(master, text="<-", bg="#7e06d4", fg="yellow", font=('Helvetica', 20, 'bold'), border=10,
                              width=2, height=1, command=Clear_Last)
        btn_Arrow.grid(row=0, column=1, padx=15, pady=10)
        btnModulus = tk.Button(master, text="%", bg="#7e06d4", fg="yellow", font=('Helvetica', 20, 'bold'), border=10,
                               width=2, height=1, command=ModularDivision)
        btnModulus.grid(row=0, column=2, padx=15, pady=10)
        btn_Division = tk.Button(master, text="/", bg="#7e06d4", fg="yellow", font=('Helvetica', 20, 'bold'), border=10,
                                 width=2, height=1, command=Division)
        btn_Division.grid(row=0, column=3, padx=15, pady=10)

        btn7 = tk.Button(master, text="7", bg="#7e06d4", fg="yellow", font=('Helvetica', 20, 'bold'), border=10,
                         width=2, height=1, command=lambda: Insert_Number('7'))
        btn7.grid(row=1, column=0, padx=15, pady=10)
        btn8 = tk.Button(master, text="8", bg="#7e06d4", fg="yellow", font=('Helvetica', 20, 'bold'), border=10,
                         width=2, height=1, command=lambda: Insert_Number('8'))
        btn8.grid(row=1, column=1, padx=15, pady=10)
        btn9 = tk.Button(master, text="9", bg="#7e06d4", fg="yellow", font=('Helvetica', 20, 'bold'), border=10,
                         width=2, height=1, command=lambda: Insert_Number('9'))
        btn9.grid(row=1, column=2, padx=15, pady=10)
        btn_Multiply = tk.Button(master, text="x", bg="#7e06d4", fg="yellow", font=('Helvetica', 20, 'bold'), border=10,
                                 width=2, height=1, command=Multiplication)
        btn_Multiply.grid(row=1, column=3, padx=15, pady=10)

        btn4 = tk.Button(master, text="4", bg="#7e06d4", fg="yellow", font=('Helvetica', 20, 'bold'), border=10,
                         width=2, height=1, command=lambda: Insert_Number('4'))
        btn4.grid(row=2, column=0, padx=15, pady=10)
        btn5 = tk.Button(master, text="5", bg="#7e06d4", fg="yellow", font=('Helvetica', 20, 'bold'), border=10,
                         width=2, height=1, command=lambda: Insert_Number('5'))
        btn5.grid(row=2, column=1, padx=15, pady=10)
        btn6 = tk.Button(master, text="6", bg="#7e06d4", fg="yellow", font=('Helvetica', 20, 'bold'), border=10,
                         width=2, height=1, command=lambda: Insert_Number('6'))
        btn6.grid(row=2, column=2, padx=15, pady=10)
        btn_subraction = tk.Button(master, text="-", bg="#7e06d4", fg="yellow", font=('Helvetica', 20, 'bold'),
                                   border=10, width=2, height=1, command=Subraction)
        btn_subraction.grid(row=2, column=3, padx=15, pady=10)

        btn1 = tk.Button(master, text="1", bg="#7e06d4", fg="yellow", font=('Helvetica', 20, 'bold'), border=10,
                         width=2, height=1, command=lambda: Insert_Number('1'))
        btn1.grid(row=3, column=0, padx=15, pady=10)
        btn2 = tk.Button(master, text="2", bg="#7e06d4", fg="yellow", font=('Helvetica', 20, 'bold'), border=10,
                         width=2, height=1, command=lambda: Insert_Number('2'))
        btn2.grid(row=3, column=1, padx=15, pady=10)
        btn3 = tk.Button(master, text="3", bg="#7e06d4", fg="yellow", font=('Helvetica', 20, 'bold'), border=10,
                         width=2, height=1, command=lambda: Insert_Number('3'))
        btn3.grid(row=3, column=2, padx=15, pady=10)
        btn_addition = tk.Button(master, text="+", bg="#7e06d4", fg="yellow", font=('Helvetica', 20, 'bold'), border=10,
                                 width=2, height=1, command=Addition)
        btn_addition.grid(row=3, column=3, padx=15, pady=10)

        btn_All_Clear = tk.Button(master, text="AC", bg="#7e06d4", fg="yellow", font=('Helvetica', 20, 'bold'),
                                  border=10, width=10, height=1, command=Clear)
        btn_All_Clear.grid(row=4, column=0, padx=15, pady=10, columnspan=2)
        btn_is_equal = tk.Button(master, text="=", bg="#7e06d4", fg="yellow", font=('Helvetica', 20, 'bold'), border=10,
                                 width=10, height=1, command=is_Equal)
        btn_is_equal.grid(row=4, column=2, padx=15, pady=10, columnspan=2)


class layout_two(layout_one):
    def __init__(self, frame_b):
        super().__init__(frame_b)

        btnSquare = tk.Button(master=frame_b, text="x^2", bg="#7e06d4", fg="yellow", font=('Helvetica', 20, 'bold'),
                              border=10, width=2, height=1, command=X_Square)
        btnSquare.grid(row=0, column=4, padx=15, pady=10)
        btn_cube = tk.Button(master=frame_b, text="x^3", bg="#7e06d4", fg="yellow", font=('Helvetica', 20, 'bold'),
                             border=10, width=2, height=1, command=X_Cube)
        btn_cube.grid(row=0, column=5, padx=15, pady=10)
        btn_x_power_n = tk.Button(master=frame_b, text="y ^ x", bg="#7e06d4", fg="yellow",
                                  font=('Helvetica', 20, 'bold'), border=10, width=2, height=1, command=Y_power_X)
        btn_x_power_n.grid(row=0, column=6, padx=15, pady=10)

        btnSquare_root = tk.Button(master=frame_b, text="_/`` ", bg="#7e06d4", fg="yellow",
                                   font=('Helvetica', 20, 'bold'), border=10, width=2, height=1, command=Square_Root)
        btnSquare_root.grid(row=1, column=4, padx=15, pady=10)
        btn_log = tk.Button(master=frame_b, text="log", bg="#7e06d4", fg="yellow", font=('Helvetica', 20, 'bold'),
                            border=10, width=2, height=1, command=Log_10)
        btn_log.grid(row=1, column=5, padx=15, pady=10)
        btn_factorial = tk.Button(master=frame_b, text="x!", bg="#7e06d4", fg="yellow", font=('Helvetica', 20, 'bold'),
                                  border=10, width=2, height=1, command=Factorial)
        btn_factorial.grid(row=1, column=6, padx=15, pady=10)

        btnSin = tk.Button(master=frame_b, text="Sin", bg="#7e06d4", fg="yellow", font=('Helvetica', 20, 'bold'),
                           border=10, width=2, height=1, command=Sine)
        btnSin.grid(row=2, column=4, padx=15, pady=10)
        btnCos = tk.Button(master=frame_b, text="Cos", bg="#7e06d4", fg="yellow", font=('Helvetica', 20, 'bold'),
                           border=10, width=2, height=1, command=Cosine)
        btnCos.grid(row=2, column=5, padx=15, pady=10)
        btnTan = tk.Button(master=frame_b, text="Tan", bg="#7e06d4", fg="yellow", font=('Helvetica', 20, 'bold'),
                           border=10, width=2, height=1, command=Tan)
        btnTan.grid(row=2, column=6, padx=15, pady=10)

        btnSinh = tk.Button(master=frame_b, text="Sinh", bg="#7e06d4", fg="yellow", font=('Helvetica', 18, 'bold'),
                            border=10, width=2, height=1, command=SineH)
        btnSinh.grid(row=3, column=4, padx=15, pady=10)
        btnCosh = tk.Button(master=frame_b, text="Cosh", bg="#7e06d4", fg="yellow", font=('Helvetica', 18, 'bold'),
                            border=10, width=2, height=1, command=CosineH)
        btnCosh.grid(row=3, column=5, padx=15, pady=10)
        btnTanh = tk.Button(master=frame_b, text="Tanh", bg="#7e06d4", fg="yellow", font=('Helvetica', 18, 'bold'),
                            border=10, width=2, height=4, command=TanH)
        btnTanh.grid(row=3, column=6, padx=15, pady=10, rowspan=2)

        btnPi = tk.Button(master=frame_b, text="`/\`", bg="#7e06d4", fg="yellow", font=('Helvetica', 20, 'bold'),
                          border=10, width=2, height=1, command=Insert_Pi)
        btnPi.grid(row=4, column=4, padx=15, pady=10)
        btnE_power_X = tk.Button(master=frame_b, text="e^x", bg="#7e06d4", fg="yellow", font=('Helvetica', 20, 'bold'),
                                 border=10, width=2, height=1, command=Exp)
        btnE_power_X.grid(row=4, column=5, padx=15, pady=10)


#     --->  Instance of Frame widgets regarding to Both the classes as discussed above    <----

global frame_a
global frame_b
global entry_frame
frame_a = Frame(root, relief='raised', bg='#150015')
frame_b = Frame(root, relief='raised', bg='#150015')
entry_frame = Frame(root, relief='raised')
entry = Entry(entry_frame, font=('Helvetica', 28, 'bold'), bd=10, bg="#3DE86E", width=30)
entry.pack(fill=X)

root.mainloop()
