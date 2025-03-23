capacity = 255
tank_filled = 0

n = int(input())

for i in range(n):
    litters = int(input())
    if tank_filled + litters > capacity:
        print(f"Insufficient capacity!")
    else:
        tank_filled += litters

print(tank_filled)
