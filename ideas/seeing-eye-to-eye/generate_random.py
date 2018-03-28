import random

n = 10**6
m = 1000

HIGH = 10**8

print(n, m)

values = random.sample(range(HIGH), n + m)
print(" ".join(map(str, sorted(values[:n]))))
print(" ".join(map(str, sorted(values[n:]))))
