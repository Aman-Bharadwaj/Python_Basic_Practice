# Highest Marks
marks = {
    "Aman": 85,
    "Rahul": 72,
    "Vansh": 90,
    "John": 88 
}

topper = ""
highest = 0

for student in marks:
    if marks[student] > highest:
        highest = marks[student]
        topper = student
        
print("Topper:", topper)

# Second highest marks
marks = {
    "Aman": 85,
    "Rahul": 72,
    "Vansh": 90,
    "John": 88 
}

values = list(marks.values())
values.sort(reverse=True)

second_highest = values[1]

for student, score in marks.items():
    if score == second_highest:
        print("Second Topper", student)