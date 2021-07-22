# Python program to create a simple GUI calculator using Tkinter

# Importing Tkinter module
from tkinter import *

# Global variable to store expression to calculate
expression = ""

# Function to update expression
def keyPress(num):
    # pointing to the global expression variable
    global expression

    # adding new item to the expression
    expression = expression + str(num)


# Driver code
if __name__ == "__main__":
    fgcolor = '#000'
    bgcolor1 = '#fff'
    bgcolor2 = 'gray'

    # creating GUI window
    root = Tk()

    # window title
    root.title("Calculator")

    # window size
    root.geometry('300x400')

    # variable class to finalize the expression
    equation = StringVar()

    # expression entry box
    expression_box = Entry(root, textvariable=equation)

    # placing the expression box in the window
    expression_box.grid(row=0,columnspan=4, ipadx=85,ipady=10,pady=15)

    # creating buttons and placing them in positions
    # upon pressing the button, respective command is executed
    one = Button(root, text='1',fg=fgcolor,bg=bgcolor1, 
    command=lambda: keyPress(1),height=3,width=7)
    one.grid(row=4,column=0,pady=5)

    two = Button(root, text='2',fg=fgcolor,bg=bgcolor1, 
    command=lambda: keyPress(2),height=3,width=7)
    two.grid(row=4,column=1,pady=5)

    three = Button(root, text='3',fg=fgcolor,bg=bgcolor1, 
    command=lambda: keyPress(3),height=3,width=7)
    three.grid(row=4,column=2,pady=5)

    four = Button(root, text='4',fg=fgcolor,bg=bgcolor1, 
    command=lambda: keyPress(4),height=3,width=7)
    four.grid(row=3,column=0,pady=5)

    five = Button(root, text='5',fg=fgcolor,bg=bgcolor1, 
    command=lambda: keyPress(5),height=3,width=7)
    five.grid(row=3,column=1,pady=5)

    six = Button(root, text='6',fg=fgcolor,bg=bgcolor1, 
    command=lambda: keyPress(6),height=3,width=7)
    six.grid(row=3,column=2,pady=5)

    seven = Button(root, text='7',fg=fgcolor,bg=bgcolor1, 
    command=lambda: keyPress(7),height=3,width=7)
    seven.grid(row=2,column=0,pady=5)

    eight = Button(root, text='8',fg=fgcolor,bg=bgcolor1, 
    command=lambda: keyPress(8),height=3,width=7)
    eight.grid(row=2,column=1,pady=5)

    nine = Button(root, text='9',fg=fgcolor,bg=bgcolor1, 
    command=lambda: keyPress(9),height=3,width=7)
    nine.grid(row=2,column=2,pady=5)

    zero = Button(root, text='0',fg=fgcolor,bg=bgcolor1, 
    command=lambda: keyPress(0),height=3,width=7)
    zero.grid(row=5,column=0,pady=5)

    point = Button(root, text='.',fg=fgcolor,bg=bgcolor1, 
    command=lambda: keyPress('.'),height=3,width=7)
    point.grid(row=5,column=1,pady=5)

    plus = Button(root, text='+',fg=fgcolor,bg=bgcolor2, 
    command=lambda: keyPress('+'),height=3,width=7)
    plus.grid(row=2,column=3,pady=5)

    minus = Button(root, text='-',fg=fgcolor,bg=bgcolor2, 
    command=lambda: keyPress('-'),height=3,width=7)
    minus.grid(row=3,column=3,pady=5)

    multiply = Button(root, text='*',fg=fgcolor,bg=bgcolor2, 
    command=lambda: keyPress('*'),height=3,width=7)
    multiply.grid(row=4,column=3,pady=5)

    divide = Button(root, text='/',fg=fgcolor,bg=bgcolor2, 
    command=lambda: keyPress('/'),height=3,width=7)
    divide.grid(row=5,column=3,pady=5)

    clear = Button(root, text='AC',fg=fgcolor,bg=bgcolor2,height=3,width=7)
    clear.grid(row=6,column=3)

    exit = Button(root, text='Exit',fg=fgcolor,bg=bgcolor2,height=3,width=7)
    exit.grid(row=6,column=2)

    equals = Button(root, text='=',fg=fgcolor,bg=bgcolor2,height=3,width=7)
    equals.grid(row=5,column=2,pady=5)

    # start the program
    root.mainloop()
