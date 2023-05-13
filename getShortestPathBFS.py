'''

Description: Find shortest path between two specified nodes using BFS.
Author: Olivia Clarke-Edwards

'''

def reconstructPath(start, end, parents):
    path = []
    current = end

    while not current == None:
        path.append(current)
        current = parents[current]
    path.reverse()
    if path[0] == start:
        return path
    return []
    

def bfsTraverseFrom(graph, n, start):
    q = []
    q.append(start)

    visited = [False for _ in range(n)]
    visited[start] = True

    parents = [None for _ in range(n)]

    while not len(q) == 0:
        current = q.pop(0)
        neighbours = graph[current]

        for next in neighbours:
            if not visited[next]:
                q.append(next)
                visited[next] = True
                parents[next] = current
    return parents


def bfs(graph, n, start, end):
    parents = bfsTraverseFrom(graph, n, start)
    return reconstructPath(start, end, parents)


def test(graph, start, end):
    n = len(graph)
    return bfs(graph, n, start, end)

graph1 = [[1], [2], [3, 5], [2, 4], [2, 3], [2, 6], [5, 7, 8], [6], [6]]
graph2 = [[1], [0], [3, 4], [2, 4], [2, 3]]

print(test(graph1, 1, 8))
print(test(graph2, 1, 4))
print(test([[0]], 0, 0))

