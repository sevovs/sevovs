message = input()

command = input()

while command != "Reveal":
    command = command.split(":|:")
    action = command[0]

    if action == "InsertSpace":
        index = int(command[1])
        message = message[0:index] + " " + message[index:]

    elif action == "Reverse":
        substring = command[1]
        if substring in message:
            message = message.replace(substring, "", 1) + substring[::-1]
        else:
            print("error")
            command = input()
            continue
    elif action == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        if substring in message:
            message = message.replace(substring, replacement)

    print(message)

    command = input()

print(f"You have a new text message: {message}")
