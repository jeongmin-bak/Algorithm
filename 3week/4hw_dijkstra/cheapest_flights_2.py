import collections
import heapq
from typing import List


def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    graph = collections.defaultdict(list)
    for u,v,w in flights:
        graph[u].append((v,w))

    q = [(0, src, k)]

    while q:
        price, node, K = heapq.heappop(q)
        if node == dst:
            return price
        if K >= 0:
            for v,w in graph[node]:
                alt = price + w
                heapq.heappush(q, (alt, v, K-1))
    return -1
