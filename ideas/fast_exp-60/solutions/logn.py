MOD = 10**9 + 7

def fast_exp(b, e):
    if e == 0:
        return 1
    else:
        d = (fast_exp(b, e // 2)**2) % MOD
        return d if e % 2 == 0 else (d * b) % MOD

# print(fast_exp(3, 1000000))
t = int(input())
for _ in range(t):
    n = int(input())
    print(fast_exp(3, n))
