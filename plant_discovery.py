number = int(input())

d = {}
k = {}
for i in range(number):
    info = input().split("<->")
    plant = info[0]
    rarity = int(info[1])

    if plant not in d.keys():
        d[plant] = rarity
    else:
        d[plant] += rarity

command = input()

while command != "Exhibition":
    command = command.split(": ")
    text = command[1].split(" - ")
    action = command[0]
    plant = text[0]
    if plant not in d:
        print("error")
    else:
        if action == "Rate":
            rating = text[1]
            if plant not in k.keys():
                k[plant] = [int(rating)]
            else:
                k[plant].append(int(rating))

        elif action == "Update":
            new_rarity = text[1]
            d[plant] = new_rarity
        elif action == "Reset":
            del k[plant]

    command = input()

print("Plants for the exhibition:")
for n in d.keys():
    if n in k.keys():
        print(f"- {n}; Rarity: {d[n]}; Rating: {sum(k[n]) / len(k[n]):.2f}")
    else:
        print(f"- {n}; Rarity: {d[n]}; Rating: 0.00")
