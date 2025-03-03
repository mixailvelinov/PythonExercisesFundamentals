def sum_numbers(a, b):
    return a + b


def subtract(a, b, c):
    return sum_numbers(a, b) - c


num1 = int(input())
num2 = int(input())
num3 = int(input())


print(subtract(num1, num2, num3))