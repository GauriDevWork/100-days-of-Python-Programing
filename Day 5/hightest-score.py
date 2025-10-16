student_score = [78, 65, 89, 90, 55, 91, 64, 89, 73, 88, 84, 77, 99, 81, 70, 185]
highest_score = 0
for score in student_score:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")