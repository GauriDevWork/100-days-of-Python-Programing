import random
import my_custom_module
a= input("Enter first number in range: ")
b = input("Enter second number in range: ")
random_number = random.randint(int(a), int(b))
print(random_number)
print(my_custom_module.my_fav_number)    