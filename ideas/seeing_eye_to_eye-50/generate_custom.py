import itertools

foos = list(itertools.chain(
    (_ for _ in range(1000,  2000, 611)),

    (_ for _ in range(20000, 21000, 61)),
    (_ for _ in range(23000, 24000, 71)),
    (_ for _ in range(24000, 25000, 61)),
    (_ for _ in range(25000, 26000, 71)),
    (_ for _ in range(50000, 200000, 10)),

))
bars = list(itertools.chain(
    (_ for _ in range(0, 100, 12)),
    (_ for _ in range(11030, 12000, 71)),
    (_ for _ in range(12030, 13000, 61)),

    (_ for _ in range(300000, 400000, 701)),
))

print(len(foos), len(bars))
print(" ".join(map(str, foos)))
print(" ".join(map(str, bars)))
