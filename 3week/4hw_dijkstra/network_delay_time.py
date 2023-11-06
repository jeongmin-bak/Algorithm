import collections
import heapq

def network_delay_time(times, n, k):
    graph = collections.defaultdict(list)
    for time in times:
        a, b, c = time
        graph[a].append((b,c))

    dist = collections.defaultdict(int)
    q = [[0,k]]

    while q:
        acc, cur = heapq.heappop(q)

        if cur not in dist:
            dist[cur] = acc
            for adj, d in graph[cur]:
                cost = acc + d
                heapq.heappush(q, (cost, adj))

    if len(dist) == n:
        return max(dist.values())
    return -1


times = [[2,1,1],[2,3,1],[3,4,1]]
n, k = 4, 2
#times = [[1,2,1]]
#n = 2
#k = 1
print(network_delay_time(times, n, k))