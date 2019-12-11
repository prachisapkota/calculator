# Simple calculator using tkinter.


from tkinter import *
import tkinter.font as font

expression=" "

def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)

def clear():
    global expression
    expression=" "
    equation.set(expression)

def equalpress():
    try:
        global expression
        total= str(eval(expression))
        equation.set(total)
        expression=" "
    except:
        equation.set("error")
        expression=" "

root=Tk()
root.title("CALCULATOR")
root.geometry("400x500")
root.resizable(0,0)
root.config(background="white")
fonttype=font.Font(family='Helvatica')
fontsize=font.Font(size=14)
fontweight=font.Font(weight='bold')



equation=StringVar()
expression_field=Entry(root,textvariable=equation, font=fontsize)
expression_field.place(relx=0.02, rely=0.02, height=75, width=380)

button1=Button(root,text='1', command=lambda :press(1) ,height=4, width =7)
button1.place(relx=0.02, rely=0.2)


button2=Button(root,text='2',command=lambda :press(2), height=4, width=7)
button2.place(relx=0.27, rely=0.2)
button3=Button(root,text='3',command=lambda :press(3), height=4, width=7)
button3.place(relx=0.52, rely=0.2)
button4=Button(root, text='Clear',command=clear,height=4, width=7)
button4.place(relx=0.77, rely=0.2)
button5=Button(root,text='4',command=lambda :press(4), height=4, width=7)
button5.place(relx=0.02, rely=0.37)
button6=Button(root,text='5',command=lambda :press(5), height=4, width=7)
button6.place(relx=0.27, rely=0.37)
button7=Button(root,text='6',command=lambda :press(6), height=4, width=7)
button7.place(relx=0.53,rely=0.37)
button8=Button(root,text='+',command=lambda :press("+"), height=4, width=7)
button8.place(relx=0.77, rely=0.37)
button9=Button(root, text='7',command=lambda :press(7), height=4, width=7)
button9.place(relx=0.02, rely=0.54)
button10=Button(root, text='8',command=lambda:press(8), height=4, width=7)
button10.place(relx=0.27, rely=0.54)
button11=Button(root,text='9',command=lambda:press(9), height=4, width=7)
button11.place(relx=0.53, rely=0.54)
button12=Button(root, text='-',command=lambda :press('-'), height=4, width=7)
button12.place(relx=0.77, rely=0.54)
button13=Button(root,text='0',command=lambda :press(0),height=4, width=7)
button13.place(relx=0.02, rely=0.71)
button14=Button(root, text='.',command=lambda :press('.'),height=4, width=7)
button14.place(relx=0.27, rely=0.71)
button15=Button(root, text='square',command=lambda :press("**2"), height=4, width=7)
button15.place(relx=0.53, rely=0.71)
button16=Button(root, text='/',command=lambda :press('/'), height=4, width=7)
button16.place(relx=0.77, rely=0.71)
button17=Button(root,text='=',command=lambda :equalpress(),height=3, width=44)
button17.place(relx=0.02, rely=0.87)


root.mainloop()
