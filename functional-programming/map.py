
def start_withA(s):
    return s[0] == "A"



fruit = ["A","B","C","D"]
mapobject = map(start_withA,fruit)

print(list(mapobject))