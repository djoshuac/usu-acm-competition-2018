
if __name__ == "__main__":
    no_same = {}

    n = int(input())
    market = [
        tuple(map(int, input().split()))
        for _ in range(n)
    ]

    for h in market:
        if h in no_same:
            print(h, "is already a house")
            raise "No duplicates constraint failed"
        if h[0] > 10**6 or h[0] < 0:
            print(h, "failed X constraint")
            raise "Failed size constraint"
        if h[1] > 10**6 or h[1] < 0:
            print(h, "failed X constraint")
            raise "Failed size constraint"
        if h[2] > 10 or h[2] < 0:
            print(h, "failed X constraint")
            raise "Failed size constraint"
