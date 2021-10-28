# isinstance(instance,class) it allow us to check particular object is instance of a class
# if we dont have any value to be assigned then no need of init method



class User:
    def sign_in(self):
        print("logged in")

    def attack(self):
        print("do nothing")

class Wizard(User):
    def __init__(self,name,power):
        self.name = name
        self.power = power
    def attack(self):
        User.attack(self)
        print(f'attacking with {self.power}')

class Archer(User):
    def __init__(self,name,num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    def attack(self):
        print(f'attacking with arrows arrows left:{self.num_arrows}')

wizard1 = Wizard("vindhya",10)
print(wizard1.attack())
archer1 = Archer("vindhya",20)
print(archer1.attack())
# to check particular object is an instance of the class
print(isinstance(wizard1,Wizard))
print(isinstance(wizard1,object))
# we can use introspection to check to which and all we have access to
print(dir(wizard1))
