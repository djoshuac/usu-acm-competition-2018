from random import randint

n = 10**6
m = 10**6

N_LOW = 0
N_HIGH = 10**10
M_LOW = 0
M_HIGH = 10**10

print(n, m)
print(" ".join(map(str, sorted(randint(M_LOW, M_HIGH) for _ in range(n)))))
print(" ".join(map(str, sorted(randint(M_LOW, M_HIGH) for _ in range(m)))))
