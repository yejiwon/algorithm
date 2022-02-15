import sys
sys.stdin = open('input.txt')

if __name__ == "__main__":
    n, k = map(int, input().split())
    pascals = [[1 for _ in range(i)] for i in range(1, 31)]

    for i in range(2, n):
        for j in range(1, i):
            pascals[i][j] = pascals[i-1][j-1] + pascals[i-1][j]

    print(pascals[n-1][k-1])
