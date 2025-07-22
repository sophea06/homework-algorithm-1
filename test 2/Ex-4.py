# 4 How many odd number in array
number = [1,3,4,5,6,9,2]
count = 0
for i in range(len(number)):
    if number[i] % 2 == 1:
        number[i] += count
        count+=1
print(count)