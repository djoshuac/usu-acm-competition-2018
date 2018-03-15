from random import randint

test0 = "sample test"
test1 = "first 10 numbers"
# test2 = 10 ** 2
# test3 = 10 ** 2
# test4 = 10 ** 2
# test4 = 10 ** 2

N_MAX = 10 ** 10
T = 100

print(T)
for _ in range(T):
    print(randint(1, N_MAX))
