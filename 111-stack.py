class Stack:
    def __init__(self):
        self.items = []  
  
    def push(self, item):
        self.items.insert(0, item)
    
    def pop(self):
        return self.items.pop(0)
    
    def print_stack(self):
        print(self.items)
    
my_stack = Stack()
my_stack.push('1')
my_stack.push('2')
my_stack.push('3')
my_stack.print_stack()

my_stack.pop()
my_stack.print_stack()

# =======
# Result:
# =====================================
# ['3', '2', '1']
# ['2', '1']
# =====================================