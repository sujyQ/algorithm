from collections import deque

def solution(maps):
    
    x = [1, 0, -1, 0]
    y = [0, 1, 0, -1]
    
    n, m = len(maps[0]), len(maps)
    visited = [[0 for _ in range(n)] for _ in range(m)]
    queue = deque([[0, 0, 2]])
    visited[0][0] = 1
    
    while queue :
        cur_x, cur_y, count = queue.popleft()

        for _x, _y in zip(x, y) :
            move_x, move_y = cur_x + _x, cur_y + _y
            if move_x < n and move_x >= 0 and move_y < m and move_y >= 0 \
                    and maps[move_y][move_x]==1 and visited[move_y][move_x] == 0:
                visited[move_y][move_x] = count
                queue.append([move_x, move_y, count+1])

    return visited[-1][-1] if visited[-1][-1] != 0 else -1
        