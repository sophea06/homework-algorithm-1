# 2 Replace all even number to 100
number = [1,3,4,5,6,9,2]
for i in range(len(number)):
    if number[i] % 2 == 0:
        number[i] =100
print(number)
