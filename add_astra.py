import re

text = input()

regex = r"(#|\|)(?P<food>([A-Za-z\s])+)\1(?P<day>\d{2}/\d{2}/\d{2})\1(?P<calories>\d+)\1"

result = re.finditer(regex, text)

output = []

total_calories = 0
for match in result:
    output.append([match.group("food"), match.group("day"), match.group("calories")])
    total_calories += int(match.group("calories"))

print(f"You have food to last you for: {int(total_calories / 2000)} days!")
for k in output:
    print(f"Item: {k[0]}, Best before: {k[1]}, Nutrition: {k[2]}")
