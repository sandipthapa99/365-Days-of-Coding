class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
    
    def __str__(self):
        return (self.name + ' (' + str(self.capacity) + 'L)')
    
    def __add__(self, other):
        self.name = self.name + ' & ' + other.name + ' Mix'
        self.capacity = self.capacity + other.capacity
        return self.__str__
    
first = Juice('Orange', 1.5)
second = Juice('Avocado', 2.0)

print(first.__add__(second)())

