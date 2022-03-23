import re

text = input()
regex = r"(::|\*\*)(?P<word>[A-Z][a-z]{2,})\1"
pattern = r"\d"

result = re.finditer(regex, text)
k = re.findall(pattern, text)


d = []
for match in result:
    d.append(match.group())

total_sum = int(k[0])

for i in range(1, len(k)):
    total_sum *= int(k[i])


new_list = []

for word in d:
    order = 0
    for ch in word:
        if ch.isalnum():
            order += ord(ch)
    if order > total_sum:
        new_list.append(word)


print(f"Cool threshold: {total_sum}")
print(f"{len(d)} emojis found in the text. The cool ones are:")
for k in new_list:
    print(k)
