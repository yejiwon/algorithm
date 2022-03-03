import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1
    if visited[x][y] != -1:  # 이미 지나온 경로
        return visited[x][y]

    # 지나오지 않은 경로
    visited[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] < graph[x][y]:
                visited[x][y] += dfs(nx, ny)

    return visited[x][y]


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[-1]*m for _ in range(n)]    # DP table

    print(dfs(0, 0))
