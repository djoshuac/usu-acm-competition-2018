from random import randint

n = 10000
m = 10000

N_LOW = 0
N_HIGH = 10**7
M_LOW = 0
M_HIGH = 10**7

print(n, m)
print(" ".join(str(randint(M_LOW, M_HIGH)) for _ in range(n)))
print(" ".join(str(randint(M_LOW, M_HIGH)) for _ in range(m)))
