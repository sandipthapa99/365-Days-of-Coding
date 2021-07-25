from tkinter import *
import tkinter.messagebox

root = Tk()
root.geometry("1100x500")
root.resizable(0,0)
root.title("Tic Tac Toe")

MainFrame = Frame(root, bg='#282C35',bd=10,padx=2,pady=2,width=1350,height=600,relief=RIDGE)
MainFrame.grid(row=0,column=0)

LeftFrame = Frame(MainFrame, bg='#282C35',bd=10,width=750,height=500,pady=2,padx=10,relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(MainFrame, bg='#282C35',bd=10,width=560,height=500,pady=2,padx=20,relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame, bg='#282C35',bd=10,width=560,height=200,pady=2,padx=10,relief=RIDGE)
RightFrame1.grid(row=0,column=0,padx=6,pady=20)

RightFrame2 = Frame(RightFrame, bg='#282C35',bd=10,width=560,height=400,pady=2,padx=10,relief=RIDGE)
RightFrame2.grid(row=1,column=0,padx=6,pady=20)

PlayerX=IntVar()
PlayerO=IntVar()

PlayerX.set(0)
PlayerO.set(0)

button = StringVar()

clickcount = 0
click = True
matchFound = False

def checker(buttons):
    global click
    global clickcount
    if buttons["text"] == "" and click ==True:
        buttons["text"] = "X"
        clickcount = clickcount+ 1
        click = False
        score()
    elif buttons["text"] == "" and click ==False:
        buttons["text"] = "O"
        clickcount =clickcount+ 1
        click = True
        score()
    # print(clickcount)
    # print(matchFound)
    
    if clickcount == 9 and matchFound == False:
        tkinter.messagebox.showinfo("Game Over", "Draw.")


def score():
    global matchFound
    if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X"):
        matchFound = True
        button1.configure(background='#00b894')
        button2.configure(background='#00b894')
        button3.configure(background='#00b894')
        n = PlayerX.get()
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Game Over", "Player X won.")
        reset()
    elif (button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X"):
        matchFound = True
        button4.configure(background='#00b894')
        button5.configure(background='#00b894')
        button6.configure(background='#00b894')
        n = PlayerX.get()
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Game Over", "Player X won.")
        reset()
    elif (button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X"):
        matchFound = True
        button7.configure(background='#00b894')
        button8.configure(background='#00b894')
        button9.configure(background='#00b894')
        n = PlayerX.get()
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Game Over", "Player X won.")
        reset()
    elif (button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X"):
        matchFound = True
        button1.configure(background='#00b894')
        button4.configure(background='#00b894')
        button7.configure(background='#00b894')
        n = PlayerX.get()
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Game Over", "Player X won.")
        reset()
    elif (button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X"):
        matchFound = True
        button2.configure(background='#00b894')
        button5.configure(background='#00b894')
        button8.configure(background='#00b894')
        n = PlayerX.get()
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Game Over", "Player X won.")
        reset()
    elif (button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):
        matchFound = True
        button3.configure(background='#00b894')
        button6.configure(background='#00b894')
        button9.configure(background='#00b894')
        n = PlayerX.get()
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Game Over", "Player X won.")
        reset()
    elif (button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X"):
        matchFound = True
        button1.configure(background='#00b894')
        button5.configure(background='#00b894')
        button9.configure(background='#00b894')
        n = PlayerX.get()
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Game Over", "Player X won.")
        reset()
    elif (button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):
        matchFound = True
        button3.configure(background='#00b894')
        button5.configure(background='#00b894')
        button7.configure(background='#00b894')
        n = PlayerX.get()
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Game Over", "Player X won.")
        reset()

    
    

    elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O"):
        matchFound = True
        button1.configure(background='#0097e6')
        button2.configure(background='#0097e6')
        button3.configure(background='#0097e6')
        n = PlayerO.get()
        score = n+1
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Game Over", "Player O won.")
        reset()
    elif (button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O"):
        matchFound = True
        button4.configure(background='#0097e6')
        button5.configure(background='#0097e6')
        button6.configure(background='#0097e6')
        n = PlayerO.get()
        score = n+1
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Game Over", "Player O won.")
        reset()
    elif (button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O"):
        matchFound = True
        button7.configure(background='#0097e6')
        button8.configure(background='#0097e6')
        button9.configure(background='#0097e6')
        n = PlayerO.get()
        score = n+1
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Game Over", "Player O won.")
        reset()
    elif (button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O"):
        matchFound = True
        button1.configure(background='#0097e6')
        button4.configure(background='#0097e6')
        button7.configure(background='#0097e6')
        n = PlayerO.get()
        score = n+1
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Game Over", "Player O won.")
        reset()
    elif (button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O"):
        matchFound = True
        button2.configure(background='#0097e6')
        button5.configure(background='#0097e6')
        button8.configure(background='#0097e6')
        n = PlayerO.get()
        score = n+1
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Game Over", "Player O won.")
        reset()
    elif (button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O"):
        matchFound = True
        button3.configure(background='#0097e6')
        button6.configure(background='#0097e6')
        button9.configure(background='#0097e6')
        n = PlayerO.get()
        score = n+1
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Game Over", "Player O won.")
        reset()
    elif (button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O"):
        matchFound = True
        button1.configure(background='#0097e6')
        button5.configure(background='#0097e6')
        button9.configure(background='#0097e6')
        n = PlayerO.get()
        score = n+1
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Game Over", "Player O won.")
        reset()
    elif (button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O"):
        matchFound = True
        button3.configure(background='#0097e6')
        button5.configure(background='#0097e6')
        button7.configure(background='#0097e6')
        n = PlayerO.get()
        score = n+1
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Game Over", "Player O won.")
        reset()

    

def reset():
    global matchFound
    global clickcount
    button1["text"] = ""
    button2["text"] = ""
    button3["text"] = ""
    button4["text"] = ""
    button5["text"] = ""
    button6["text"] = ""
    button7["text"] = ""
    button8["text"] = ""
    button9["text"] = ""
    clickcount = 0
    matchFound = False

    button1.configure(background='gainsboro')
    button2.configure(background='gainsboro')
    button3.configure(background='gainsboro')
    button4.configure(background='gainsboro')
    button5.configure(background='gainsboro')
    button6.configure(background='gainsboro')
    button7.configure(background='gainsboro')
    button8.configure(background='gainsboro')
    button9.configure(background='gainsboro')

def newGame():
    reset()
    PlayerX.set(0)
    PlayerO.set(0)

labelPlayerx = Label(RightFrame1,font=('arial',30,'bold'),text='Player X :',padx=2,pady=2,bg='#282C35',fg='White')
labelPlayerx.grid(row=0,column=0,sticky=W,pady=5)
txtPlayerx = Entry(RightFrame1,font=('arial',30,'bold'),bd=2,fg='#282C35',textvariable=PlayerX,width=8, justify=CENTER).grid(row=0,column=1,pady=5)

labelPlayero = Label(RightFrame1,font=('arial',30,'bold'),text='Player O :',padx=2,pady=2,bg='#282C35',fg='White')
labelPlayero.grid(row=1,column=0,sticky=W)
txtPlayer0 = Entry(RightFrame1,font=('arial',30,'bold'),bd=2,fg='#282C35',textvariable=PlayerO,width=8, justify=CENTER).grid(row=1,column=1)

resetbtn = Button(RightFrame2,text="Restart",font=('Arial',30,'bold'),height=1,width=15,command=reset)
resetbtn.grid(row=2,column=0, padx=6,pady=10)

newbtn = Button(RightFrame2,text="New Game",font=('Arial',30,'bold'),height=1,width=15,command=newGame)
newbtn.grid(row=3,column=0,padx=6,pady=10)


button1 = Button(LeftFrame,text="",font=('TImes 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button1))
button1.grid(row=1,column=0,sticky=S+N+E+W)

button2 = Button(LeftFrame,text="",font=('TImes 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button2))
button2.grid(row=1,column=1,sticky=S+N+E+W)

button3 = Button(LeftFrame,text="",font=('TImes 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button3))
button3.grid(row=1,column=2,sticky=S+N+E+W)

button4 = Button(LeftFrame,text="",font=('TImes 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button4))
button4.grid(row=2,column=0,sticky=S+N+E+W)

button5 = Button(LeftFrame,text="",font=('TImes 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button5))
button5.grid(row=2,column=1,sticky=S+N+E+W)

button6 = Button(LeftFrame,text="",font=('TImes 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button6))
button6.grid(row=2,column=2,sticky=S+N+E+W)

button7 = Button(LeftFrame,text="",font=('TImes 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button7))
button7.grid(row=3,column=0,sticky=S+N+E+W)

button8 = Button(LeftFrame,text="",font=('TImes 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button8))
button8.grid(row=3,column=1,sticky=S+N+E+W)

button9 = Button(LeftFrame,text="",font=('TImes 26 bold'),height=3,width=8,bg='gainsboro',command=lambda:checker(button9))
button9.grid(row=3,column=2,sticky=S+N+E+W)


root.mainloop()