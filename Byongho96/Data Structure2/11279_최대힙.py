# [0, 1, 1, 2, 2, 2, 2, 3, 3, 3]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
class MaxHeap:
    def __init__(self, maxsize):
        self.MAX_SIZE = maxsize
        self.size = 0
        self.lst = []
    def parent(self, curIdx):
        return curIdx // 2
    def leftchild(self, curIdx):
        return curIdx * 2 +1
    def rightchild(self, curIdx):
        return curIdx * 2 +2
    def swap(self, curIdx, parentIdx):
        self.lst[curIdx], self.lst[parentIdx] = self.lst[parentIdx], self.lst[curIdx]

    def maxHeapify(self, i):
        i = i

    def insert(self, n):
        if self.size == self.MAX_SIZE:
            return
        curIdx = self.size
        self.lst[curIdx] = n
        self.size += 1
        while n > self.lst[self.parent(curIdx)]:
            self.swap(curIdx, self.parent(curIdx))
            curIdx = self.parent(curIdx)

    def delete(self):
        if not self.size:
            return
        self.size -= 1
        self.swap(0, self.size)
        return self.lst.pop()
        self.maxHeapify(0)
