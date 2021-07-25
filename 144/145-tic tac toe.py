from tkinter import *
import tkinter.messagebox

root = Tk()
root.geometry("1100x500")
# root.resizable(0,0)
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

labelPlayerx = Label(RightFrame1,font=('arial',30,'bold'),text='Player X :',padx=2,pady=2,bg='#282C35',fg='White')
labelPlayerx.grid(row=0,column=0,sticky=W,pady=5)
txtPlayerx = Entry(RightFrame1,font=('arial',30,'bold'),bd=2,fg='#282C35',textvariable=PlayerX,width=8, justify=LEFT).grid(row=0,column=1,pady=5)

labelPlayero = Label(RightFrame1,font=('arial',30,'bold'),text='Player O :',padx=2,pady=2,bg='#282C35',fg='White')
labelPlayero.grid(row=1,column=0,sticky=W)
txtPlayer0 = Entry(RightFrame1,font=('arial',30,'bold'),bd=2,fg='#282C35',textvariable=PlayerO,width=8, justify=LEFT).grid(row=1,column=1)

resetbtn = Button(RightFrame2,text="Reset",font=('Arial',30,'bold'),height=1,width=15)
resetbtn.grid(row=2,column=0, padx=6,pady=10)

newbtn = Button(RightFrame2,text="New Game",font=('Arial',30,'bold'),height=1,width=15)
newbtn.grid(row=3,column=0,padx=6,pady=10)


button1 = Button(LeftFrame,text="",font=('TImes 26 bold'),height=3,width=8,bg='gainsboro')
button1.grid(row=1,column=0,sticky=S+N+E+W)

button2 = Button(LeftFrame,text="",font=('TImes 26 bold'),height=3,width=8,bg='gainsboro')
button2.grid(row=1,column=1,sticky=S+N+E+W)

button3 = Button(LeftFrame,text="",font=('TImes 26 bold'),height=3,width=8,bg='gainsboro')
button3.grid(row=1,column=2,sticky=S+N+E+W)

button4 = Button(LeftFrame,text="",font=('TImes 26 bold'),height=3,width=8,bg='gainsboro')
button4.grid(row=2,column=0,sticky=S+N+E+W)

button5 = Button(LeftFrame,text="",font=('TImes 26 bold'),height=3,width=8,bg='gainsboro')
button5.grid(row=2,column=1,sticky=S+N+E+W)

button6 = Button(LeftFrame,text="",font=('TImes 26 bold'),height=3,width=8,bg='gainsboro')
button6.grid(row=2,column=2,sticky=S+N+E+W)

button7 = Button(LeftFrame,text="",font=('TImes 26 bold'),height=3,width=8,bg='gainsboro')
button7.grid(row=3,column=0,sticky=S+N+E+W)

button8 = Button(LeftFrame,text="",font=('TImes 26 bold'),height=3,width=8,bg='gainsboro')
button8.grid(row=3,column=1,sticky=S+N+E+W)

button9 = Button(LeftFrame,text="",font=('TImes 26 bold'),height=3,width=8,bg='gainsboro')
button9.grid(row=3,column=2,sticky=S+N+E+W)



root.mainloop()