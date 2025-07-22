# 6 Sum only even number in array
number = [1,3,4,5,6,9,2]
sum = 0
for i in range(len(number)):
    if number[i] % 2 == 0:
        sum += number[i]
print(sum)