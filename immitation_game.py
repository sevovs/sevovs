message = input()

command = input()

while command != "Decode":
    text = command.split("|")
    action = text[0]

    if action == "Move":
        number_of_letters = int(text[1])
        message = message[number_of_letters:] + message[0:number_of_letters]
    elif action == "Insert":
        index = int(text[1])
        value = text[2]
        message = message[0:index] + value + message[index:]
    elif action == "ChangeAll":
        substring = text[1]
        replacement = text[2]
        while substring in message:
            message = message.replace(substring, replacement)

    command = input()


print(f"The decrypted message is: {message}")