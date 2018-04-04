def is_worse(h, v):
    return all(
        a <= b
        for a, b in zip(h, v)
    )

def is_top_tier(h, market):
    return not(any(
        is_worse(h, v)
        for v in market if h != v
    ))

def solution(market):
    return sum(
        1 if is_top_tier(h, market) else 0
        for h in market
    )


if __name__ == "__main__":
    n = int(input())
    market = [
        tuple(map(int, input().split()))
        for _ in range(n)
    ]
    print(solution(market))
