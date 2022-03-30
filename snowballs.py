number_of_snowballs = int(input())
best_snowball_quality = 0
best_snowball_data = ""
for i in range(number_of_snowballs):
    weight_of_snowball = int(input())
    time = int(input())
    quality = int(input())
    result = (weight_of_snowball / time) ** quality
    if result > best_snowball_quality:
        best_snowball_quality = result
        best_snowball_data = f"{weight_of_snowball} : {time} = {int(result)} ({quality})"
print(best_snowball_data)
