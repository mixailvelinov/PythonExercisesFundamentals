# Calculate how many courses will be needed to elevate N persons by using an elevator with a capacity of P persons.
# The input holds two lines: the number of people N and the capacity P of the elevator.

def calculate_elevator_courses(people, capacity):
    if people % capacity != 0:
        result = people // capacity + 1
    else:
        result = people // capacity

    return result


total_people = int(input())
elevator_capacity = int(input())

print(calculate_elevator_courses(total_people, elevator_capacity))


