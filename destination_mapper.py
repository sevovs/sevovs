import re

text = input()

regex = r"([=|/])([A-Z][A-Za-z]{2,})\1"

result = re.finditer(regex, text)

output = []
total_sum = 0
for match in result:
    output.append(match.group(2))
    total_sum += len(match.group(2))

print(f"Destinations: {', '.join(output)}")
print(f"Travel Points: {total_sum}")
