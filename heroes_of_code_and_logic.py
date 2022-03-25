number = int(input())

d = {}

for i in range(number):
    info = input().split()
    hero = info[0]
    HP = int(info[1])
    MP = int(info[2])

    d[hero] = [HP, MP]

command = input()

while command != "End":
    command = command.split(" - ")
    action = command[0]
    hero = command[1]

    if action == "CastSpell":
        mp_needed = int(command[2])
        spell_name = command[3]
        if d[hero][1] >= mp_needed:
            d[hero][1] -= mp_needed
            print(f"{hero} has successfully cast {spell_name} and now has {d[hero][1]} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")

    elif action == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        d[hero][0] -= damage
        if d[hero][0] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {d[hero][0]} HP left!")
        else:
            del d[hero]
            print(f"{hero} has been killed by {attacker}!")
    elif action == "Recharge":
        amount = int(command[2])
        if d[hero][1] + amount < 200:
            d[hero][1] += amount
            print(f"{hero} recharged for {amount} MP!")
        else:
            diff = abs(200 - d[hero][1])
            d[hero][1] = 200
            print(f"{hero} recharged for {diff} MP!")
    elif action == "Heal":
        amount = int(command[2])
        if d[hero][0] + amount < 100:
            d[hero][0] += amount
            print(f"{hero} healed for {amount} HP!")
        else:
            diff = abs(100 - d[hero][0])
            d[hero][0] = 100
            print(f"{hero} healed for {diff} HP!")

    command = input()


for k in d.keys():
    print(f"{k}")
    print(f"  HP: {d[k][0]}")
    print(f"  MP: {d[k][1]}")
