numbers = [int(num) for num in input().split()]
count = int(input())

for num in range(count):
    numbers.remove(min(numbers))

print(', '.join([str(num) for num in numbers]))
