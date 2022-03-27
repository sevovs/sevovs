number = int(input())

d = {}

for i in range(number):
    info = input().split("|")
    piece = info[0]
    composer = info[1]
    key = info[2]

    if piece not in d.keys():
        d[piece] = [composer, key]

command = input()

while command != "Stop":
    text = command.split("|")
    action = text[0]
    piece = text[1]

    if action == "Add":
        composer = text[2]
        key = text[3]
        if piece not in d.keys():
            d[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif action == "Remove":
        if piece in d.keys():
            del d[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif action == "ChangeKey":
        new_key = text[2]
        if piece in d.keys():
            d[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

for k in d.keys():
    print(f"{k} -> Composer: {d[k][0]}, Key: {d[k][1]}")
