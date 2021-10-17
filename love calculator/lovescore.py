print("Welcome to Love Calculator")
name1 = input("Enter Your Name?")
name2 = input("Enter their Name?")

name_c = name1.lower() + name2.lower()

t = name_c.count("t")
r = name_c.count("r")
u = name_c.count("u")
e = name_c.count("e")

l = name_c.count("l")
o = name_c.count("o")
v = name_c.count("v")
e = name_c.count("e")

true = t + r + u + e
love = l + o + v + e
score = str(true) + str(love)

if int(score) < 10 or int(score) > 90:

  print(f"Your score is {score}, you go together like coke and mentos.")

elif 40 >=int(score)  and int(score) <= 50:

  print(f"Your score is {score}, you are alright together.")

else:

  print(f"Your score is {score}.")