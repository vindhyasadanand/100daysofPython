class PlayGame:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def run(self):
        print(f"My name is {self.name}")

player1 = PlayGame('vindhya',21)
player2 = PlayGame('sandhya',28)

print(player1.name)
print(player2.name)

player1.run()