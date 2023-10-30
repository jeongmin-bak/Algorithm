import time
def quicksort(lst, start, end):
    def partition(part, ps, pe):
        pivot = lst[pe]
        i = ps-1

        for j in range(ps, pe):
            if part[j] <= pivot:
                i += 1
                part[i], part[j] = part[j], part[i]

        part[i+1], part[pe] = part[pe], part[i+1]
        return i+1

    if start >= end:
        return None

    p = partition(lst, start, end)
    quicksort(lst, start, p-1)
    quicksort(lst, p, end)

    return lst

#quicksort pivot을 맨 앞을 기준으로

def quicksort_2(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left, right = list(), list()

    for index in range(1, len(data)):
        if pivot > data[index]:
            left.append(data[index])
        else:
            right.append(data[index])

    return quicksort_2(left) + [pivot] + quicksort_2(right)


def quicksort_3(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    left = right = list()

    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot <= item]

    return quicksort_3(left) + [pivot] + quicksort_3(right)

lst = [1,6,2,9,4]


print(quicksort(lst,0,len(lst)-1))

print(quicksort_2(lst))

print(quicksort_3(lst))
