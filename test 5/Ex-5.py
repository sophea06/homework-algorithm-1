studentsList = [
    {"id": 1, "name": "John", "age": 20, "gender": "male", "class": "A"},
    {"id": 2, "name": "Jane", "age": 21, "gender": "female", "class": "B"},
    {"id": 3, "name": "Bob", "age": 22, "gender": "male", "class": "C"},
    {"id": 4, "name": "Alice", "age": 23, "gender": "female", "class": "A"},
    {"id": 5, "name": "Tom", "age": 24, "gender": "male", "class": "B"},
    {"id": 6, "name": "Lucy", "age": 25, "gender": "female", "class": "B"},
    {"id": 7, "name": "Jack", "age": 26, "gender": "male", "class": "A"},
]
#5 - Which class has the most students?
countMostStudent = 0
# for key in studentsList:
#     if key['id'] == '1':
countA = 0
countB = 0
countC = 0
for key in studentsList:
    if key['class'] == "A":
        countA += 1
    if key['class'] == 'B':
        countB += 1
    if key["class"] == 'C':
        countC +=1
    if countA > countB:
        countMostStudent+=1
    if countB > countC:
       countMostStudent += 1
    if countA > countC:
        countMostStudent += 1
    if countC > countA:
        countMostStudent += 1
    if countC > countB:
        countMostStudent += 1
print(countMostStudent)
    


