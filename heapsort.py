import heapq

class MaxHeap:
    def __init__(self):
        self.heap_array = [None]

    def __len__(self):
        return len(self.heap_array)-1
    def _percolate_up(self):
        cur = len(self)

        parent = cur // 2
        while parent > 0:
            if self.heap_array[cur] > self.heap_array[parent]:
                self.heap_array[cur], self.heap_array[parent] = self.heap_array[parent], self.heap_array[cur]

            cur = parent
            parent = cur // 2

    def _percolate_down(self, cur):
        biggest = cur
        left = 2*cur
        right = 2*cur + 1

        if left <= len(self) and self.heap_array[left] > self.heap_array[biggest]:
            biggest = left
        if right <= len(self) and self.heap_array[right] > self.heap_array[biggest]:
            biggest = right

        if biggest != cur:
            self.heap_array[cur], self.heap_array[biggest] = self.heap_array[biggest], self.heap_array[cur]
            self._percolate_down(biggest)

    def insert(self, data):
        if len(self) <= 1:
            self.heap_array.append(data)
            return

        self.heap_array.append(data)
        self._percolate_up()

    def extract(self):
        if len(self) < 1:
            return None

        root = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        self.heap_array.pop()
        self._percolate_down(1)

        return root


def sorted_by_heap(lst):
    maxheap = MaxHeap()
    for elem in lst:
        maxheap.insert(elem)

    desc = [maxheap.extract() for _ in range(len(lst))]
    return list(reversed(desc))


lst = [8,3,6,1,2]
print(lst)
