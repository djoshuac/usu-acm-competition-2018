from collections import namedtuple

MAX_POOLS = 20
b, t, p = (0, 1, 2)

def solution(market):
    count = 0
    max_t_given_p = [-1] * (MAX_POOLS + 1)
    market.sort(reverse=True)
    for h in market:
        if h[t] > max_t_given_p[h[p]]:
            count += 1
            for i in range(h[p], -1, -1):
                if max_t_given_p[i] > h[t]:
                    break
                max_t_given_p[i] = max(h[t], max_t_given_p[i])
    return count


if __name__ == "__main__":
    n = int(input())
    market = [
        tuple(map(int, input().split()))
        for _ in range(n)
    ]
    print(solution(market))
