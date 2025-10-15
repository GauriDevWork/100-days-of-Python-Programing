print("Welcome to the RollerCoaster!")
height = int(input("What is your height in cm? "))
ticket_price = 0
if height >= 120:
    age = int(input("What is your age? "))
    if age < 12:
        ticket_price = 5
    elif age <= 18:
        ticket_price = 7
    elif age >=45 and age <=55:
        ticket_price = 0
    else:
        ticket_price = 12
    photo = input("Do you want a photo taken? y or n. ")
    if photo == "y":
        ticket_price += 3
    print(f"Your final ticket price is ${ticket_price}.")
else:
    print("Sorry, you have to be taller to ride the rollercoaster.")