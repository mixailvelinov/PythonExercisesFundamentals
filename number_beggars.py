#more compelx solution using dictionaries

numbers = [int(num) for num in input().split(", ")]
beggars_count = int(input())
beggars_results = {}
list_result = []


while numbers:
    for beggar in range(1, beggars_count + 1):

        if beggar not in beggars_results and len(numbers) == 0:
            beggars_results[beggar] = [0]
            continue

        if len(numbers) == 0:
            break

        elif beggar not in beggars_results:
            beggars_results[beggar] = [numbers[0]]

        elif beggar in beggars_results:
            beggars_results[beggar].append(numbers[0])

        del numbers[0]


for key, value in beggars_results.items():
    list_result.append(sum(value))

print(list_result)


#easier solution using lists only

numbers = [int(num) for num in  input().split(', ')]
beggars = int(input())

beggars_list = [0] * beggars

for i, num in enumerate(numbers):
    beggars_list[i % beggars] += num

print(beggars_list)