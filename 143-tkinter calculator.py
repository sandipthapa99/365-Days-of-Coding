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

    # updating expression using set method

# Driver code

if __name__ == "__main__":
    # creating GUI window
    root = Tk()

    # window title
    root.title("Calculator")

    # window size
    root.geometry('400x150')

    # variable class to finalize the expression
    equation = StringVar()

    # expression entry box
    expression_box = Entry(root, textvariable=equation)

    # placing the expression box in the window
    expression_box.grid(columnspan=4, ipadx=100)

    # creating buttons and placing them in positions
    # upon pressing the button, respective command is executed
    one = Button(root, text='1',fg='black',bg='white', command=lambda: keyPress(1),height=1,width=7)
    one.grid(row=4,column=0)

    two = Button(root, text='2',fg='black',bg='white', command=lambda: keyPress(1),height=1,width=7)
    two.grid(row=4,column=1)

    three = Button(root, text='3',fg='black',bg='white', command=lambda: keyPress(1),height=1,width=7)
    three.grid(row=4,column=2)

    four = Button(root, text='4',fg='black',bg='white', command=lambda: keyPress(1),height=1,width=7)
    four.grid(row=3,column=0)

    five = Button(root, text='5',fg='black',bg='white', command=lambda: keyPress(1),height=1,width=7)
    five.grid(row=3,column=1)

    six = Button(root, text='6',fg='black',bg='white', command=lambda: keyPress(1),height=1,width=7)
    six.grid(row=3,column=2)

    seven = Button(root, text='7',fg='black',bg='white', command=lambda: keyPress(1),height=1,width=7)
    seven.grid(row=2,column=0)

    eight = Button(root, text='8',fg='black',bg='white', command=lambda: keyPress(1),height=1,width=7)
    eight.grid(row=2,column=1)

    nine = Button(root, text='9',fg='black',bg='white', command=lambda: keyPress(1),height=1,width=7)
    nine.grid(row=2,column=2)

    zero = Button(root, text='0',fg='black',bg='white', command=lambda: keyPress(1),height=1,width=7)
    zero.grid(row=5,column=1)

    point = Button(root, text='.',fg='black',bg='white', command=lambda: keyPress(1),height=1,width=7)
    point.grid(row=5,column=2)

    plus = Button(root, text='+',fg='black',bg='gray', command=lambda: keyPress(1),height=1,width=7)
    plus.grid(row=2,column=3)

    minus = Button(root, text='-',fg='black',bg='gray', command=lambda: keyPress(1),height=1,width=7)
    minus.grid(row=3,column=3)

    multiply = Button(root, text='*',fg='black',bg='gray', command=lambda: keyPress(1),height=1,width=7)
    multiply.grid(row=4,column=3)

    divide = Button(root, text='/',fg='black',bg='gray', command=lambda: keyPress(1),height=1,width=7)
    divide.grid(row=5,column=3)

    clear = Button(root, text='AC',fg='black',bg='gray', command=lambda: keyPress(1),height=1,width=7)
    clear.grid(row=6,column=0)

    equals = Button(root, text='+',fg='black',bg='gray', command=lambda: keyPress(1),height=1,width=7)
    equals.grid(row=6,column=1)

    

    

    
    # start the program
    root.mainloop()
