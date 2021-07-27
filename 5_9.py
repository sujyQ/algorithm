from collections import dequeue

##########################################
# BFS : Breadth First Search
# 1. push start node to queue and check it's visited
# 2. pop node and push all of its not-yet visited adjacency nodes to queue and check it's visited
# 3. repeat 2 till it cannot be executed
##########################################
def bfs(graph, start, visited) :
    # use deque library for queue
    queue = dequeue([start])
    # check that start node is visited
    visited[start] = True
    # repeat untill queue is empty
    while queue :
        # pop
        v = queue.popleft()
        print(v, end=' ')
        # push all of its not-yet visited adjacency nodes
        for i in graph[v] :
            if not visited :
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph=graph, v=1, visited=visited)  # 1 2 3 8 7 4 5 6