# 6 Delete dara and theara from list
students = ['bopha','dara','kanha','theara']
newArray = []
for i in range(len(students)):
    if students[i] != "dara" and students[i] != "theara":
        newArray.append(students[i])
print(newArray)