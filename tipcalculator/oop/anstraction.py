# hiding the information and giving access to those which are necessary

class PlayerCharacter:
    def __init__(self,name,age):
        self._name = name 
        self._age = age

    def run(self):
        print('run')
    

    def speak(self):
        print(f'my name is {self._name} and I am {self._age} years old')

player2 = PlayerCharacter('sandhya',29)

player2.run()
player2.speak()