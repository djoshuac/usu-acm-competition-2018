no_same = {}

n, m = map(int, input().split())
foos = list(map(int, input().split()))
bars = list(map(int, input().split()))

last = -1
for i, f in enumerate(foos):
    if f <= last:
        print(i, f)
        raise "Foos do not all increase"
    if f in no_same:
        raise str(f) + " already exists in set"
    no_same[f] = True
    last = f

last = -1
for i, b in enumerate(bars):
    if b <= last:
        print(i, b)
        raise "Bars do not all increase"
    if b in no_same:
        raise str(b) + " already exists in set"
    no_same[b] = True
    last = b
