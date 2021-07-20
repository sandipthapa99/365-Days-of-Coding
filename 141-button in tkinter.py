from tkinter import *   
 
# create a tkinter window
root = Tk()  

# window title
root.title(" My Program")
 
# window dimension
root.geometry('200x100')
 
# Create a Button and close the window on clicking it
btn = Button(root, text = 'Click to Exit!', bd = '10',
            command = root.destroy)
 
# Setting the position of button on the top of window.  
btn.pack(side = 'top')   
 
root.mainloop()