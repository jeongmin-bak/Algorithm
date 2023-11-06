import heapq
import sys

INF = int(1e9)
def mar(graph):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    dist = [[INF]*N for _ in range(N)]
    q = [(graph[0][0], 0, 0)] #가중치, x, y
    dist[0][0] = graph[0][0]

    while q:
        acc, x, y = heapq.heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                cost = graph[nx][ny] + acc
                if dist[nx][ny] > cost:
                    dist[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

    return dist[N-1][N-1]
with open('testcase_mars.txt') as f:
    sys.stdin = f
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        N = int(input())
        graph = []
        for _ in range(N):
            graph.append(list(map(int, input().split())))
        print(mar(graph))