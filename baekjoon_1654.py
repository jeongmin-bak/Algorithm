import sys

# 입력
K, N = map(int, input().split())
lines = list(map(int, input().split()))

#n, k = 4, 11
#lines = [802,743,457,539]
lines.sort()

start, end = 1, max(lines)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in lines:
        cnt += i// mid

    if cnt >= N:
        start = mid + 1
    else:
        end = mid -1

print(end)