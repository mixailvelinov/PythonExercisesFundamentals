# Write a program that reads four integer numbers.
# It should add the first to the second number,
# integer divide the sum by the third number,
# and multiply the result by the fourth number.
# Print the final result.


def resolver(numbers):
    return ((numbers[0] + numbers[1]) // numbers[2]) * numbers[3]


count = 4
numbers_list = [int(input()) for i in range(count)]
print(resolver(numbers_list))



