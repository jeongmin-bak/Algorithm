import collections
import heapq
def find_cheapest_price(n, flights, src, dst, k):
    graph = collections.defaultdict(list)
    for a, b, c in flights:
        graph[a].append((b,c))

    dist = collections.defaultdict(list)
    q = [[0,src]]
    cnt = -1
    while q:
        acc, cur = heapq.heappop(q)

        if cur not in dist:
            dist[cur].append((cnt,acc))

        if(cnt < k):
            for adj, d in graph[cur]:
                cost = acc + d
                heapq.heappush(q, (cost, adj))
            cnt += 1

    if dist[dst] and dist[dst][0][0] == k:
        return dist[dst][0][1]
    return -1
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1

#n = 3
#flights = [[0,1,100],[1,2,100],[0,2,500]]
#src = 0
#dst = 2
#k = 1

#n = 3
#flights = [[0,1,100],[1,2,100],[0,2,500]]
#src = 0
#dst = 2
#k = 0
print(find_cheapest_price(n, flights, src, dst, k))