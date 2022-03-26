number = int(input())

d = {}

for i in range(number):
    info = input().split("|")
    car = info[0]
    mileage = int(info[1])
    fuel = int(info[2])

    if car not in d.keys():
        d[car] = [mileage, fuel]

command = input()

while command != "Stop":
    text = command.split(" : ")
    action = text[0]
    car = text[1]

    if action == "Drive":
        distance = int(text[2])
        fuel = int(text[3])
        if d[car][1] >= fuel:
            d[car][0] += distance
            d[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if d[car][0] >= 100000:
                print(f"Time to sell the {car}!")
                del d[car]
        else:
            print("Not enough fuel to make that ride")
    elif action == "Refuel":
        fuel = int(text[2])
        if d[car][1] + fuel < 75:
            d[car][1] += fuel
            print(f"{car} refueled with {fuel} liters")
        else:
            diff = abs(d[car][1] - 75)
            d[car][1] += diff
            print(f"{car} refueled with {diff} liters")
    elif action == "Revert":
        kilometers = int(text[2])

        if d[car][0] - kilometers < 10000:
            d[car][0] = 10000
            pass
        else:
            d[car][0] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()

for k in d.keys():
    print(f"{k} -> Mileage: {d[k][0]} kms, Fuel in the tank: {d[k][1]} lt.")
