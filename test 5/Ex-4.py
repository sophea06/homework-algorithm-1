studentsList = [
    {"id": 1, "name": "John", "age": 20, "gender": "male", "class": "A"},
    {"id": 2, "name": "Jane", "age": 21, "gender": "female", "class": "B"},
    {"id": 3, "name": "Bob", "age": 22, "gender": "male", "class": "C"},
    {"id": 4, "name": "Alice", "age": 23, "gender": "female", "class": "A"},
    {"id": 5, "name": "Tom", "age": 24, "gender": "male", "class": "B"},
    {"id": 6, "name": "Lucy", "age": 25, "gender": "female", "class": "B"},
    {"id": 7, "name": "Jack", "age": 26, "gender": "male", "class": "A"},
]
#4 - How many students are there in each class and gender?
countFamaleA = 0
countFamaleB = 0
countFamaleC = 0
countMaleA = 0
countMaleB = 0
countMaleC = 0
for key in studentsList:
    if key['class'] == 'A':
        students = key['gender']
        if key['gender'] == 'female':
            countFamaleA +=1
        if key['gender'] == 'male':
            countMaleA += 1
        result = key['class']

    if key['class'] == 'B':
        students = key['gender']
        if key['gender'] == 'female':
            countFamaleB +=1
        if key['gender'] == 'male':
            countMaleB += 1
        result_b = key['class']

    if key['class'] == 'C':
        students = key['gender']
        if key['gender'] == 'female':
            countFamaleC +=1
        if key['gender'] == 'male':
            countMaleC += 1
        result_c = key['class']

print("For class",result,"student has famale is",countFamaleA,"and","student has male is",countMaleA)
print("For class",result_b,"student has famale is",countFamaleB,"and","student has male is",countMaleB)
print("For class",result_c,"student has famale is",countFamaleC,"and","student has male is",countMaleC)
