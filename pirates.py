info = input()

d = {}

while info != "Sail":
    info = info.split("||")
    cities = info[0]
    population = int(info[1])
    gold = int(info[2])

    if cities not in d:
        d[cities] = [population, gold]
    else:
        d[cities][0] += population
        d[cities][1] += gold
    info = input()

command = input()

while command != "End":
    command = command.split("=>")
    action = command[0]
    cities = command[1]

    if action == "Plunder":
        people = int(command[2])
        gold = int(command[3])
        d[cities][0] -= people
        d[cities][1] -= gold
        print(f"{cities} plundered! {gold} gold stolen, {people} citizens killed.")
        if d[cities][0] == 0 or d[cities][1] == 0:
            print(f"{cities} has been wiped off the map!")
            del d[cities]
    elif action == "Prosper":
        gold = int(command[2])

        if gold > 0:
            d[cities][1] += gold
            print(f"{gold} gold added to the city treasury. {cities} now has {d[cities][1]} gold.")
        else:
            print("Gold added cannot be a negative number!")

    command = input()

if len(d) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(d.keys())} wealthy settlements to go to:")
    for k in d.keys():
        print(f"{k} -> Population: {d[k][0]} citizens, Gold: {d[k][1]} kg")
