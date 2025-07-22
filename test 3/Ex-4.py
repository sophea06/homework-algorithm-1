# 4 How many letter "n" in array
fruits = ['banana','coconut']
count = 0
for i in range(len(fruits)):
    fruit = fruits[i]
    for j in range(len(fruit)):
        if fruits[i][j] == "n":
            count += 1
print(count)