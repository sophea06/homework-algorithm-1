# 7 Remove coconu
fruits = ['banana','coconut']
# fruits.remove("coconut")
# fruits.pop(1)
index = None
for i in range(len(fruits)):
    if fruits[i] == "coconut":
        index = i
fruits.pop(index)
print(fruits)
