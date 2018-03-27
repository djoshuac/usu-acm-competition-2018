INF = 10**20

def binary_search(a, values):
    l, h = 0, len(values) - 1
    while True:
        if l >= h:
            return l
        m = l + h
        b = values[m]
        if a == b:
            return m
        elif a < b:
            h =  m - 1
        else:
            l = m

def nearest(a, values):
    x = binary_search(a, values)
    if x == len(values) - 1:
        c, d = x - 1, x
    else:
        c, d = x, x + 1
    return nearest_to(a, [values[c], values[d]])

def nearest_to(a, options):
    best = (-1, INF)
    for o in options:
        d = abs(a - o)
        if d < best[1]:
            best = (o, d)
    return best[0]

n, m = map(int, input().split())
foos = list(map(int, input().split()))
bars = list(sorted(map(int, input().split())))

print(min(abs(foo - nearest(foo, bars)) for foo in foos))
