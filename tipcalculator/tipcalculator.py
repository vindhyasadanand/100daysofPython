print("Welcome to tip calculator")
bill = float(input("Enter the bill amount? Rs"))
tip = int(input("How much would you like to give? 10 12 or 15"))
people = int(input("How many people to split the bill"))

bill_with_tip = (tip/100);
total_tip = bill_with_tip * bill + bill
tip_per_people= round(total_tip/people,2)
tip_per_people = "{:.2f}".format(tip_per_people)
print(f"Each person should pay  {tip_per_people}Rs")


