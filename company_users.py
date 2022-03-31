info = input()

company_users = {}

while info != "End":
    command = info.split(" -> ")
    company = command[0]
    ID = command[1]

    if company not in company_users:
        company_users[company] = []

    if ID not in company_users[company]:
        company_users[company].append(ID)
    info = input()


for key in company_users:
    print(key)
    for value in company_users[key]:
        print(f"-- {value}")