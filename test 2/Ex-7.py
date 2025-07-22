# 7 Find maximum number and minimum number in list
number = [1,3,4,5,6,9,2]
max = number[0]
min = number[0]
for i in range(len(number)):
    if number[i] > max:
        max = number[i]
    if number[i] < min :
        min = number[i]
print(max)
print(min)