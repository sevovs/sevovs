import re


number = int(input())
regex = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"

for i in range(number):
    info = input()

    if re.match(regex, info):
        digits = re.findall(r"\d", info)
        if digits:
            print(f"Product group: {''.join(digits)}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")
