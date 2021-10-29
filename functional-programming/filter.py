
def fun(variable):
    letters = ['a','b','c','d','e','f']
    if variable in letters:
        return True
    else:
        return False



sequence = ['a','e','i','o','u']

filterd = filter(fun,sequence)

for i in filterd:
    print(i)