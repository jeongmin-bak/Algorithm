from sys import stdin
#N, M = map(int, stdin.readline().split())
#lst = list(map(int, stdin.readline().split()))

N, M = 4,20
#lst = [20,15,10,17]
lst = [4,42,40,26,46]
lst.sort(reverse=True)

def binary_search(start, end):
    while True:
        mid = (start+end) // 2
        gather = 0
        for val in lst:
            if mid < val:
                gather += val - mid
        if gather == M:
            return mid
        elif gather > M:
            end = mid
        else:
            start = mid

def func(lst):
    p = 0
    while True:
        limit = lst[p]
        gather = 0
        for val in lst:
            if limit < val:
                gather += val - limit
        if gather < M:
            p += 1
        elif gather == M:
            return lst[p]
        else:
            return binary_search(lst[p-1], lst[p])

print(func(lst))

