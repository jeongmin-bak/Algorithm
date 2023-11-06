import sys
import collections
def city(graph):
    return

with open('testcase_city.txt') as f:
    INF = int(1e9)
    sys.stdin = f
    input = sys.stdin.readline

    n, m = map(int, input().split())

    dist = [[INF]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        dist[i][i] = 0

    for _ in range(m):
        a, b = map(int, input().split())
        dist[a][b] = 1
        dist[b][a] = 1

    x, k = map(int, input().split())

    for k in range(1,n+1):
        for a in range(1,n+1):
            for b in range(1,n+1):
                dist[a][b] = min(dist[a][b], dist[a][k]+ dist[k][b])
    for row in dist[1:]:
        print(' '.join([str(el) for el in row]))
    print("======")

    distance = dist[1][k] + dist[k][x]

    if distance >= INF:
        print(-1)
    else:
        print(distance)


