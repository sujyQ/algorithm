from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
icebox = []
for _ in range(N) :
    icebox.append(list(map(int, sys.stdin.readline()[:-1])))

def dfs(x, y) :
    if x <= -1 or x >= N or y <= -1 or y >= M :
        return False

    # if current node is not visited,
    if icebox[x][y] == 0 :
        icebox[x][y] = 1

        # call up, left, down, right nodes recursively
        dfs(x-1,y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        # print(i, j, 'True')
        return True
    # print(i, j, 'False')
    # if node is visited (not hole or already visited)
    return False

result = 0
for i in range(N) :
    for j in range(M) :
        if dfs(i, j) == True :
            # print(i, j)
            result += 1

print(result)


