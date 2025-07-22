# 9 Replace student name who has letter "R" contain theri name
students = ['bopha','dara','kanha','theara']
for i in range(len(students)):
    for char in students[i]:
        if char == "r":
            students[i] = "zasa"
print(students)