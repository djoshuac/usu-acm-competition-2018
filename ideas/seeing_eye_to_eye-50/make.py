import itertools

foos = list(itertools.chain(
    (_ for _ in range(1000,  2000, 611)),

    (_ for _ in range(20000, 21000, 61)),
    (_ for _ in range(21000, 22000, 71)),
    (_ for _ in range(22000, 23000, 61)),
    (_ for _ in range(23000, 24000, 71)),
    (_ for _ in range(24000, 25000, 61)),
    (_ for _ in range(25000, 26000, 71)),
    (_ for _ in range(26000, 27000, 61)),
    (_ for _ in range(27000, 28000, 701)),
    (_ for _ in range(27000, 28000, 701)),
    (_ for _ in range(50000, 200000, 10)),
    (_ for _ in range(1000000, 1100100, 3)),
    (_ for _ in range(4000000, 7100100, 3)),

))
bars = list(itertools.chain(
    (_ for _ in range(0, 100, 12)),
    (_ for _ in range(3000,  4000, 51)),
    (_ for _ in range(4000,  5000, 55)),
    (_ for _ in range(6000,  7000, 90)),
    (_ for _ in range(7000,  8000, 79)),
    (_ for _ in range(8000,  9000, 71)),
    (_ for _ in range(10030, 11000, 65)),
    (_ for _ in range(11030, 12000, 71)),
    (_ for _ in range(12030, 13000, 61)),
    (_ for _ in range(13030, 19000, 71)),
    (_ for _ in range(27049, 30000, 701)),
    (_ for _ in range(300000, 400000, 701)),
    (_ for _ in range(8000000, 9100100, 3)),
))

print(len(foos), len(bars))
print(" ".join(map(str, foos)))
print(" ".join(map(str, bars)))
