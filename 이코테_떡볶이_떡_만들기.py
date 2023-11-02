#K, N = map(int, input().split())
#lines = list(map(int, input().split()))

n,m = 4, 6
lines = [19, 15, 10, 17]
lines.sort()

start, end = 1, max(lines)
while start <= end:
    mid = (start+end) // 2
    length = 0
    for i in lines:
        if mid < i:
            length += i - mid

    if length >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)