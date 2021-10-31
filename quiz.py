print("Welcome to Quiz game!")

playing = input("Do you want to Play? Yes or No")

if playing.lower()!="yes":
    quit()
print("Okey Lets Play :)")
score = 0

answer = input("What does CPU stands for?")

if answer.lower() =="central processing unit":
    print("Correct!")
    score +=1

else:
    print("Incorrect!!")


answer = input("What does RAM Stands for?")

if answer.lower() =="random access memory":
    print("Correct!")
    score +=1

else:
    print("Incorrect!!")

answer = input("What does GPU stands for?")

if answer.lower() =="graphics processing unit":
    print("Correct!")
    score +=1

else:
    print("Incorrect!!")
answer = input("What does ROM stands for?")

if answer.lower() =="read only memory":
    print("Correct!")
    score +=1

else:
    print("Incorrect!!")

print(f"You got {score} questions correct!!")
print(f"{(score//4)*100}% Result")