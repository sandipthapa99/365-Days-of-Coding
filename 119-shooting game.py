# parent class
class Enemy:
    name = ""
    lives = 0
    def __init__(self,name,lives):
        self.name = name
        self.lives = lives
    
    def hit(self):
        self.lives -= 1
        if self.lives <= 0:
            print(self.name,"killed!")
        else:
            print(self.name,"has",self.lives,"lives")

# Inheriting from Monster class
class Monster(Enemy):
    def __init__(self):
        super().__init__("Monster", 3)

class Alien(Enemy):
    def __init__(self):
        super().__init__("Alien", 3)

# Object initialization
mn = Monster()
al = Alien()

# hit input
while True:
    x = input()
    if x == "laser":
        al.hit()
    elif x == "gun":
        mn.hit()
    elif x == "stop":
        break

# =====================================================
#     Input:        |              Result:
# =====================================================
#     gun           |          Monster has 2 lives
#     laser         |          Alien has 2 lives
#     gun           |          Monster has 1 lives
#     gun           |          Monster killed!
#     laser         |          Alien has 1 lives
#     laser         |          Alien Killed!
#     laser         |      
#     stop          |
# =====================================================