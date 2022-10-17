print("Welcome to the tip calculator")

bill = float(input("How much was the bill?  "))
people = int(input("How many people is it being split between?  "))
tipPercentage = int(input("What percentage do you want to tip?  "))

amtToPay = "{:.2f}".format(round((bill / people) * ((tipPercentage/100) + 1), 2))

print(f"Each person should pay ${amtToPay}")
