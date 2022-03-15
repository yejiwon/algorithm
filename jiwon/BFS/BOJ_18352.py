from collections import deque
import sys
sys.stdin = open('input.txt')

n, m, k, x = map(int, input().split())
dist = [-1] * (n+1)  # 출발도시 x 에 대한 최단거리 기록
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

dq = deque()
dq.append(x)
dist[x] = 0

while dq:
    now = dq.popleft()
    for next in graph[now]:
        if dist[next] == -1:
            dist[next] = dist[now] + 1
            dq.append(next)

check = False
for i in range(1, n+1):
    if dist[i] == k:
        print(i)
        check = True

if not check:
    print(-1)
