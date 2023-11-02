import sys
from collections import Counter

# 입력
#n, m = map(int, sys.stdin.readline().split())
#trees = Counter(map(int, sys.stdin.read().split()))
n,m = 4,20
#lst = [20,15,10,17]
trees = Counter([4,42,40,26,46])
# 초기 설정
s = 1
e = 1000000000

while s <= e:
    mid = (s + e) // 2  # 중간값 설정
    # 중간값을 기준으로 잘랐을 때 가져갈 수 있는 나무 길이 합 계산
    tot = sum((h - mid) * i for h, i in trees.items() if h > mid)

    if tot >= m:  # 가져갈 수 있는 나무 길이 합이 목표보다 크거나 같은 경우
        s = mid + 1  # 높이를 높여야 함
    elif tot < m:  # 가져갈 수 있는 나무 길이 합이 목표보다 작은 경우
        e = mid - 1  # 높이를 낮춰야 함

print(e)