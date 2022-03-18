from collections import deque
import sys
sys.stdin = open('input.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

EMPTY = 0

# 1. data set
n, k = map(int, input().split())

graph = []
virus = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != EMPTY:
            virus.append((graph[i][j], 0, i, j))

s, x, y = map(int, input().split())


# 2. 로직
virus.sort()    # 바이러스 순으로 정렬
dq = deque(virus)

while dq:       # 비선점이므로 자동으로 작은 바이러스부터 확산
    v, t, xx, yy = dq.popleft()
    if t == s:
        break
    for i in range(4):
        nx = xx + dx[i]
        ny = yy + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == EMPTY:
                graph[nx][ny] = v
                dq.append((v, t+1, nx, ny))

print(graph[x-1][y-1])
