from collections import deque
graph = {
    1:[2,3,4],
    2:[5],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[3]
}

def bfs_queue(start):
    visited = [start]
    queue = deque([start])

    while queue:
        top = queue.popleft()
        for adj in graph[top]:
            if adj not in visited:
                queue.append(adj)
                visited.append(adj)
    return visited
print(bfs_queue(1))
