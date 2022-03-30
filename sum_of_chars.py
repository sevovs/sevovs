# print(ord("a"))
# print(chr(97))

number = int(input())
total_sum = 0

for num in range(1, number + 1):
    char = input()
    total_sum += ord(char)
print(f"The sum equals: {total_sum}")