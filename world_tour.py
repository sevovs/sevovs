destination = input()

command = input()

while command != "Travel":
    text = command.split()
    action = text[0]

    if action == "Add":
        text = text[1].split(":")
        index = int(text[1])
        city = text[2]
        if index < len(destination):
            destination = destination[0:index] + city + destination[index:]
    elif action == "Remove":
        text = text[1].split(":")
        start_index = int(text[1])
        end_index = int(text[2])
        if start_index < len(destination) and end_index < len(destination):
            destination = destination[0:start_index] + destination[end_index + 1:]
    else:
        switch = command.split(":")
        old_string = switch[1]
        new_string = switch[2]

        if old_string in destination:
            destination = destination.replace(old_string, new_string)

    print(destination)

    command = input()


print(f"Ready for world tour! Planned stops: {destination}")
