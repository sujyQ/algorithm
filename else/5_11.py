import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())

miro = []
for _ in range(N) :
    miro.append(list(map(int, sys.stdin.readline()[:-1])))

def bfs(graph, start_x, start_y) :
    queue = deque()
    queue.append((start_x, start_y))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue :
        x, y = queue.popleft()
        print(x, y)

        for i in range(len(dx)) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M or graph[nx][ny]==0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph

print(bfs(miro, 0, 0)[N-1][M-1])






