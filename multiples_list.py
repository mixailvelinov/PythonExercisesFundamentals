factor = int(input())
count = int(input())
numbers = []

for x in range(1, count+1):
    numbers.append(x*factor)

print(numbers)