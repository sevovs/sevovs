
countries = [x for x in input().split(", ")]
capitals = [x for x in input().split(", ")]

result = dict(zip(countries, capitals))

for key, value in result.items():
    print(f"{key} -> {value}")

