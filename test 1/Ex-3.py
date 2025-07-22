# 3 Delete number 9
number = [1,3,4,5,6,9,2]
# number.remove(9)
# print(number)

index = None
for i in range(len(number)):
    if number[i] == 9:
        index= i
number.pop(index)
print(number)