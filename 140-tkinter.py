from tkinter import * 
from tkinter.ttk import *
    
# creates main window object
root = Tk()
  
# window title
root.title(" My Program")
  
# Label shows the output on the window
my_label = Label(root, text ="Hello World !").pack()
  
# mainloop tells the code to keep displaying 
root.mainloop()