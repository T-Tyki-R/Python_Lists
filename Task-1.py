# Python List Transformation

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
grades.reverse()

# average = sum(grades) / len(grades) returns a decimal 
average = sum(grades) // len(grades)
print(average)

grades = grades[0:7]
failure = ["Failed"] * 3
print(grades + failure)