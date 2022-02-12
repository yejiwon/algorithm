from itertools import combinations
import sys

HOUSE = 1
CHICKEN = 2

MAX_VALUE = sys.maxsize


def distance(c, h):
    return abs(c[0] - h[0]) + abs(c[1] - h[1])


if __name__ == "__main__":
    chickens = []
    houses = []

    n, m = map(int, input().split())
    for i in range(n):
        arr = list(map(int, input().split()))
        for j in range(n):
            if arr[j] == HOUSE:
                houses.append((i, j))
            if arr[j] == CHICKEN:
                chickens.append((i, j))

    res = MAX_VALUE

    for selected in list(combinations(chickens, m)):
        sum = 0
        for h in houses:
            minDist = MAX_VALUE
            for s in selected:
                minDist = min(minDist, distance(h, s))
            sum += minDist
        res = min(sum, res)

    print(res)
