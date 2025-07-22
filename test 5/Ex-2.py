studentsList = [
    {"id": 1, "name": "John", "age": 20, "gender": "male", "class": "A"},
    {"id": 2, "name": "Jane", "age": 21, "gender": "female", "class": "B"},
    {"id": 3, "name": "Bob", "age": 22, "gender": "male", "class": "C"},
    {"id": 4, "name": "Alice", "age": 23, "gender": "female", "class": "A"},
    {"id": 5, "name": "Tom", "age": 24, "gender": "male", "class": "B"},
    {"id": 6, "name": "Lucy", "age": 25, "gender": "female", "class": "B"},
    {"id": 7, "name": "Jack", "age": 26, "gender": "male", "class": "A"},
]
#2 - How many students are there in each class?
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
print("Student has in class A is",countA)
print("Student has in class B is",countB)
print("Student has in class C is",countC)
