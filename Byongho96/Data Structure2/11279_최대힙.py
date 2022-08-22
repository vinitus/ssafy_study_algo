# 632ms
import sys
input = sys.stdin.readline
# [0, 1, 1, 2, 2, 2, 2, 3, 3, 3]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Maxheap filed from lst[0]
class MaxHeap:
    def __init__(self, maxsize):
        self.MAX_SIZE = maxsize
        self.size = 0
        self.lst = [None] * self.MAX_SIZE
    def parent(self, curIdx):
        if curIdx:
            return (curIdx - 1) // 2
        return 0
    def leftchild(self, curIdx):
        return curIdx * 2 + 1
    def rightchild(self, curIdx):
        return curIdx * 2 + 2
    def swap(self, curIdx, parentIdx):
        self.lst[curIdx], self.lst[parentIdx] = self.lst[parentIdx], self.lst[curIdx]

    def maxHeapify(self, i):
        lastIdx = self.size - 1
        leftIdx = self.leftchild(i)
        rightIdx = self.rightchild(i)
        
        maxIdx = i
        if leftIdx <= lastIdx and self.lst[maxIdx] < self.lst[leftIdx]:
            maxIdx = leftIdx
        if rightIdx <= lastIdx and self.lst[maxIdx] < self.lst[rightIdx]:
            maxIdx = rightIdx

        if maxIdx != i:
            self.swap(i, maxIdx)
            self.maxHeapify(maxIdx)

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
            return 0    # 문제조건
        self.size -= 1
        self.swap(0, self.size)
        self.maxHeapify(0)
        return self.lst[self.size]
    
    def Print(self):
        print(self.lst[:self.size])

heap = MaxHeap(100000)  # 최대 연산의 갯수 크기만큼
# int(input())
for _ in range(int(input())):
    N  = int(input())
# for N in map(int, (input().split())):
    if not N:
        print(heap.delete())
    else:
        heap.insert(N)