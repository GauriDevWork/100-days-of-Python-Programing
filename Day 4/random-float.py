import random
random_number_0_to_1 = random.random()  #will include 0 but exclude 1 as it is 0.0>= x <1.0
print(random_number_0_to_1)
random_number_0_to_10 = random.random()*10  #will include 0 but exclude 10 as it is 0.0>= x <10.0
print(random_number_0_to_10)
random_number_1_to_10 = random.random()*9 + 1  #will include 1 but exclude 10 as it is 1.0>= x <10.0
print(random_number_1_to_10)
random_number_1_to_100 = random.random()*99 + 1  #will include 1 but exclude 100 as it is 1.0>= x <100.0
print(random_number_1_to_100)

random_float = random.uniform(1, 10)  #will include both 1 and 10 as it is 1.0>= x <=10.0
print(random_float)