studentsList = [
    {
        "id": 1, 
        "name": "John", 
        "age": 20, 
        "scores": {
            "html": 85, 
            "algorithm": 46, 
            "english": 88,
            "pl": 90,
        }
    },
    {
        "id": 2,
        "name": "Mary",
        "age": 21,
        "scores": {
            "html": 80,
            "algorithm": 90,
            "english": 40,
            "pl": 90,
        }
    },
    {
        "id": 3,
        "name": "Mike",
        "age": 22,
        "scores": {
            "html": 70,
            "algorithm": 60,
            "english": 80,
            "pl": 70,
        }
    },
    {
        "id": 4,
        "name": "Sara",
        "age": 19,
        "scores": {
            "html": 90,
            "algorithm": 85,
            "english": 95,
            "pl": 80,
        }
    },
    {
        "id": 5,
        "name": "Tom",
        "age": 23,
        "scores": {
            "html": 75,
            "algorithm": 65,
            "english": 70,
            "pl": 60,
        }
    }

]
# 4 - Who has age greater than 20
for key in studentsList:
    if key['id'] == 1:
        age_greater  = key["age"]
    if key['age'] > 20:
        age_greater = key["age"]
    student_name = key['name']
print(age_greater)
print(student_name)