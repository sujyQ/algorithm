########################################################################
# DFS : Depth-First Search
# 1. push search start node to stack and check it's visited
# 2. if the top node of the stack has not-yet visited node, push that node and check it's visited
#    if it's not, pop the top node of the stack
# 3. repeat 1 and 2 till these can not be executed.
########################################################################

def dfs(graph, v, visited) :
    # check that current node v is visited
    visited[v] = True
    print(v, end = ' ')

    # recursively visit the node that linked with the current node
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)

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

dfs(graph=graph, v=1, visited=visited)
