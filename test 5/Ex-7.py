studentsList = [
    {"id": 1, "name": "John", "age": 20, "gender": "male", "class": "A"},
    {"id": 2, "name": "Jane", "age": 21, "gender": "female", "class": "B"},
    {"id": 3, "name": "Bob", "age": 22, "gender": "male", "class": "C"},
    {"id": 4, "name": "Alice", "age": 23, "gender": "female", "class": "A"},
    {"id": 5, "name": "Tom", "age": 24, "gender": "male", "class": "B"},
    {"id": 6, "name": "Lucy", "age": 25, "gender": "female", "class": "B"},
    {"id": 7, "name": "Jack", "age": 26, "gender": "male", "class": "A"},
]
#7 - Which class has youngest student?
for key in studentsList:
    if key['id'] == 1:
       youngest = key['age']
    if key['age'] < youngest:
        youngest = key['age']
    result = key['class']
print(youngest)
print(result)