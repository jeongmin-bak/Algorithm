import sys

#input = sys.stdin.readline
#n = int(input())  # 지방의 수
n = 4
#arr = list(map(int, input().split()))
arr = [120,110,140,150]
#m = int(input())
m = 485
start, end = 0, max(arr)
while start <= end:
    mid = (start + end) // 2
    curr = 0
    for i in arr:
        if i >= mid:
            curr += mid
        else:
            curr += i
    if curr <= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)