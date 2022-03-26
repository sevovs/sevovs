password = input()
command = input()


new_password = password

while command != "Done":
    text = command.split()
    action = text[0]

    if action == "TakeOdd":
        curr_password = new_password
        new_password = ""
        for i in range(len(curr_password)):
            if i % 2 != 0:
                new_password += curr_password[i]

        print(new_password)

    elif action == "Cut":
        index = int(text[1])
        lenght = int(text[2])
        test = new_password[index:index + lenght]
        new_password = new_password.replace(test, "", 1)
        print(new_password)
    elif action == "Substitute":
        substring = text[1]
        substitute = text[2]
        if substring in new_password:
            new_password = new_password.replace(substring, substitute)
            print(new_password)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {new_password}")
