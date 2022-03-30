number_of_lines = int(input())
capacity = 0

for i in range(number_of_lines):
    liters_of_water = int(input())
    if liters_of_water + capacity <= 255:
        capacity += liters_of_water
        continue
    print(f"Insufficient capacity!")

print(capacity)