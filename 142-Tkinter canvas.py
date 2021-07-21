from tkinter import *

# create a tkinter window
root = Tk()
# window title
root.title(" My Program")

# Label for Text Area
Label(root, text='First Name').grid(row=0)
Label(root, text='Last Name').grid(row=1)

# Initializing Entry bject for Text Boxes
textBox1 = Entry(root)
textBox2 = Entry(root)

# Placing Text Boxes
textBox1.grid(row=0, column=1)
textBox2.grid(row=1, column=1)

# Run the application
root.mainloop()

# Result:
# --------------------------------------------