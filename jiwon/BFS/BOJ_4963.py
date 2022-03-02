from collections import deque
import sys
sys.stdin = open('input.txt')


dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

SEA = 0
LAND = 1


def bfs(graph, x, y):
    dq = deque()
    dq.append((x, y))
    graph[x][y] = SEA

    while dq:
        cx, cy = dq.popleft()
        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == LAND:
                    dq.append((nx, ny))
                    graph[nx][ny] = SEA


if __name__ == "__main__":
    w, h = map(int, input().split())
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    cnt = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == LAND:
                cnt += 1
                bfs(graph, i, j)

    print(cnt)
