
#N = 4
#lst = [120,110,140,150]
#lst = [70,80,30,40,100]
lst = [140,150,200,160]
total_budget = 485
#N = int(input())
#lst = list(map(int, input().split()))

#total_budget = int(input())

lst.sort()
def binary_search(left, right, p, diff):
    t = []
    while left <= right:
        mid = (left + right) // 2
        total = sum(lst[:p]) + len(lst[p:]) * mid
        if total in t:
            break

        t.append(total)
        if total > total_budget:
            right = mid
        else:
            if total_budget - total < diff:
                diff = total_budget - total
                left = mid

    return mid


def func(lst):
    if total_budget >= sum(lst):
        return lst[-1]
    p = len(lst)-2

    while True:
        limit_budget = lst[p]
        total = sum(lst[:p])+ len(lst[p:]) * limit_budget
        if total > total_budget:
            p -= 1
            if p < 0:
                return None
                break
        else:
            return binary_search(lst[p], lst[p+1], p+1, total_budget-total)

print(func(lst))

