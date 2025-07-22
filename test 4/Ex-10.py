# 10 Add bopha and theara new list
students = ['bopha','dara','kanha','theara']
newList = []
for i in range(len(students)):
    if students[i] == "bopha" or students[i] == "theara":
        newList.append(students[i])
print(newList)  