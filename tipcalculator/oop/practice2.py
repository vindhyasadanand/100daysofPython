class PlayerWorld:
    membership = True
    #__ underscore indicates we should not modify this
    def __init__(self,name="anonymous",age=0):
        
            self.name = name
            self.age = age
    def shout(self):
        print(f'my name is {self.name}')
    #creating class method
    #if we want to modify class attributes and methods we go for classmethods
    @classmethod 
    def adding_things(cls,num1,num2):
        return num1+num2
    #static method will not have access to class state
    @staticmethod
    def adding_things2(num1,num2):
        return num1+num2

   



player1 = PlayerWorld('vindhya',21)
player2 = PlayerWorld()
player2.shout()
print(player1.adding_things(2,3))

#dict1 = {1:"vindhya", 2:"sandhya"}
#print(dict1[1])