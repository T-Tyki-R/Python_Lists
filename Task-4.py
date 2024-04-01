# Deep Dive into Python Lists

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

# Task 1 uses index/position to print
# Task 2 uses append to push values into new list and print

students_approved = [] 

for num in range(len(grades)):
    if grades[num] < 80:
        print(students[num], grades[num], activities[num])
    else:
        students_approved.append(students[num])
        
print(students_approved)
        

