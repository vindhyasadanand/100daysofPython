class Toy():
    def __init__(self,color,age):
        self.color = color
        self.age = age
    
    def __self__(self):
        return f'{self.color}'

action_figure = Toy('red',0)
print(action_figure.__str__())
#introspection = ability to find type of an object during runtime`

