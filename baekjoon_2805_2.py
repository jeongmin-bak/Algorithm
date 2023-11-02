from sys import stdin
N, M = map(int, stdin.readline().split())
#tree = list(map(int, stdin.readline().split()))
tree = [4,42,40,26,46]
start, end = 1, max(tree)


while start <= end:
    mid = (start+end) // 2
    tree_length = 0
    for i in tree:
        if mid < i:
            tree_length += i - mid

    if tree_length >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)