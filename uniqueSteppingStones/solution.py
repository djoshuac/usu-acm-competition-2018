def solution(n, m, grid):
    def has_unique(i, j, steps, already_checked):
        if j == m:
            return True
        elif grid[i][j] in steps or grid[i][j] in already_checked:
            return False
        else:
            next_already_checked = {}
            already_checked[grid[i][j]] = True
            steps.append(grid[i][j])
            if any(has_unique(i_prime, j+1, steps, next_already_checked) for i_prime in range(n)):
                return True
            else:
                steps.pop()
                return False
    already_checked = {}
    return "Yes" if any(has_unique(i, 0, [], already_checked) for i in range(n)) else "No"


if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = [
        list(map(int, input().split()))
        for _ in range(n)
    ]
    print(solution(n, m, grid), end="")
