print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
split = float(input("How many people to split the bill?"))

per_person = round(((total * (tip/100)) + total) / split, 2)

print(f"Each person should pay ${per_person}")
