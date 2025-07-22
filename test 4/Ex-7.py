# 7 How many letter "A" in list
students = ['bopha','dara','kanha','theara']
count = 0
for i in range(len(students)):
    student = students[i]
    for j in range(len(student)):
        if students[i][j] == "a":
            count +=1
print(count)