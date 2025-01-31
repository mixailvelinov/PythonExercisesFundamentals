numbers = [int(num) for num in input().split()]

list_result = [abs(num) if num < 0 else -abs(num) for num in numbers ]

print(list_result)
