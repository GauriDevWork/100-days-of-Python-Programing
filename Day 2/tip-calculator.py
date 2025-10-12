print("Welcome to the tip calculator!")
total_bill = float(input("what was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))
bill_per_person = (total_bill + (total_bill*(tip_percentage / 100))) / num_people
#print(f"Each person should pay: ${bill_per_person:.2f}")

print("Each person should pay: $" + str(format(bill_per_person, '.2f')))
