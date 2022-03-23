activation_key = input()

command = input()

while command != "Generate":
    text = command.split(">>>")
    action = text[0]

    if action == "Contains":
        substring = text[1]

        if substring in activation_key:
            print(f"{activation_key} contains {substring}")

        else:
            print("Substring not found!")
    elif action == "Flip":
        start_index = int(text[2])
        end_index = int(text[3])
        if text[1] == "Upper":
            activation_key = activation_key[0:start_index] + activation_key[
                                                             start_index:end_index].upper() + activation_key[end_index:]
            print(activation_key)
        elif text[1] == "Lower":
            activation_key = activation_key[0:start_index] + activation_key[
                                                             start_index:end_index].lower() + activation_key[end_index:]
            print(activation_key)
    elif action == "Slice":
        start_index = int(text[1])
        end_index = int(text[2])
        activation_key = activation_key[0:start_index] + activation_key[end_index:]
        print(activation_key)

    command = input()

print(f"Your activation key is: {activation_key}")
