# Class and objects

class Adder():
    # constructor method which called when an object is created
    # allows the class to initialize the attributes of a class
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    # adds two attributes
    def add(self):
        z = self.x + self.y
        return z
    
x = 100/10  # returns 10.0 
y = 2*10    # return 20

m = Adder(x,y)
print(m.add())  # returns 30.0

# --------
# Result:
# --------------------------------------------------------
# 30.0
# --------------------------------------------------------
