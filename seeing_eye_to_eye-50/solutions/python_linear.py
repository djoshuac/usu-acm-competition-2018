def solution(foos, bars):
    d_min = abs(foos[0] - bars[0])
    i = 0
    for f in foos:
        while i < len(bars) and f > bars[i]:
            i += 1
        d_min = min(d_min, abs(f - bars[i - 1]))
        d_min = min(d_min, abs(f - bars[i])) if i < len(bars) else d_min
    return d_min

n, m = map(int, input().split())
foos = list(map(int, input().split()))
bars = list(sorted(map(int, input().split())))

print(solution(foos, bars))
