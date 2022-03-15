from collections import deque
import sys
sys.stdin = open('input.txt')

EMPTY = 0
WALL = 1
VIRUS = 2

MAX_WALLS = 3

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
temp = [[0]*m for _ in range(n)]    # 맵 설치 후 벽
graph = [list(map(int, input().split())) for i in range(n)]  # 실제 벽
res = 0


def bfs(i, j):
    dq = deque()
    dq.append((i, j))
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if temp[nx][ny] == EMPTY:
                    temp[nx][ny] = VIRUS
                    dq.append((nx, ny))


def getScore(graph):
    sumVal = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == EMPTY:
                sumVal += 1
    return sumVal


def dfs(count):
    global res

    if count == MAX_WALLS:  # 최대로 설치할 수 있는 벽이면
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]
        # 바이러스 퍼뜨리고
        for i in range(n):
            for j in range(m):
                if temp[i][j] == VIRUS:
                    temp[i][j]
                    bfs(i, j)
        # 안전 영역을 계산한다.
        res = max(res, getScore(temp))
        return

    # 벽을 설치하는 경우의 수
    for i in range(n):
        for j in range(m):
            if graph[i][j] == EMPTY:
                graph[i][j] = WALL
                dfs(count+1)
                graph[i][j] = EMPTY


dfs(0)
print(res)
