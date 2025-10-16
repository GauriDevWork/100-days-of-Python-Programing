import random
print("welcome to the PyPassword Generator!")
list_of_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list_of_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list_of_symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password_list = []
for choosen_letter in range(1,len(list_of_letters)+1):
    if choosen_letter <= nr_letters:
        password_list.append(random.choice(list_of_letters))
for choosen_symbol in range(1,len(list_of_symbols)+1):
    if choosen_symbol <= nr_symbols:
        password_list.append(random.choice(list_of_symbols))    
for choosen_number in range(1,len(list_of_numbers)+1):
    if choosen_number <= nr_numbers:
        password_list.append(random.choice(list_of_numbers))
random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(f"your password is: {password}")