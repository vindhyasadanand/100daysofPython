class PlayerWorld:
    membership = True
    def __init__(self,name="anonymous",age=0):
        
            self.name = name
            self.age = age
    def shout(self):
        print(f'my name is {self.name}')
    #creating class method
    @classmethod 
    def adding_things(cls,num1,num2):
        return num1+num2


player1 = PlayerWorld('vindhya',21)
player2 = PlayerWorld()
player2.shout()
print(player1.adding_things(2,3))