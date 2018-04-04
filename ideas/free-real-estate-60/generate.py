from random import randint

n = 10 ** 6
already = set()
already.add((-1, -1, -1))

def random_bedrooms():
    return randint(0, 10**6)

def random_bathrooms():
    return randint(0, 10**6)

def random_pools():
    return randint(0, 20)

print(n)
for _ in range(n):
    house = (-1, -1, -1)
    while house in already:
        house = (random_bedrooms(), random_bathrooms(), random_pools())
    already.add(house)
    print(" ".join(map(str, house)))
