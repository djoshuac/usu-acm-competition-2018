n, m = map(int, input().split())
foos = list(map(int, input().split()))
bars = list(map(int, input().split()))

print(min(
    abs(foo - bar)
    for foo in foos
    for bar in bars
))
