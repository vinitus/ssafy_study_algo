# 직접구현 -> 시간초과: 아마 2개의 기준을 가지고 최솟값 비교하는거 때문에??
import sys
input = sys.stdin.readline
# # Maxheap filed from lst[1]
# # [max, 1, 2, 3, 4, 5, 6, ]
# class MinHeap:
#     def __init__(self, max_size):
#         self.MAX_SIZE = max_size
#         self.minheap = [0] * (self.MAX_SIZE + 1)
#         self.minheap[0] = (0, 0)
#         self.size = 0
#     def parent(self, cur_idx):
#         return cur_idx // 2
#     def leftchild(self, cur_idx):
#         return cur_idx * 2
#     def rightchild(self, cur_idx):
#         return cur_idx * 2 + 1
#     def swap(self, i, j):
#         self.minheap[i], self.minheap[j] = self.minheap[j], self.minheap[i]
#     def min_heapify(self, root_idx):
#         last_idx = self.size
#         left_idx = self.leftchild(root_idx)
#         right_idx = self.rightchild(root_idx)
#
#         min_idx = root_idx
#         if left_idx <= last_idx and self.minheap[left_idx] == min(self.minheap[left_idx], self.minheap[min_idx], key=lambda x: (x[0], x[1])):
#             min_idx = left_idx
#         if right_idx <= last_idx and self.minheap[right_idx] == min(self.minheap[right_idx], self.minheap[min_idx], key=lambda x: (x[0], x[1])):
#         # if right_idx <= last_idx and self.minheap[right_idx][0] <= self.minheap[min_idx][0] and self.minheap[right_idx][1] < self.minheap[min_idx][1]:
#             min_idx = right_idx
#
#         if min_idx != root_idx:
#             self.swap(min_idx, root_idx)
#             self.min_heapify(min_idx)
#     def insert(self, N):
#         if self.size == self.MAX_SIZE:
#             return
#         self.size += 1
#         cur_idx = self.size
#         self.minheap[self.size] = N
#         while N == min(N, self.minheap[self.parent(cur_idx)], key=lambda x: (x[0], x[1])):
#         # while N[0] <= self.minheap[self.parent(cur_idx)][0] and N[1] < self.minheap[self.parent(cur_idx)][1]:
#             self.swap(cur_idx, self.parent(cur_idx))
#             cur_idx = self.parent(cur_idx)
#     def delete(self):
#         if not self.size:
#             return (0, 0)
#         self.swap(1, self.size)
#         self.size -= 1
#         self.min_heapify(1)
#         return self.minheap[self.size + 1]
#     def Print(self):
#         print(self.minheap[:self.size+1])
#
# heap = MinHeap(100000)
# for _ in range(int(input())):
#     N = int(input())
#     if N:
#         N = (abs(N), N)
#         heap.insert(N)
#         # heap.Print()
#     else:
#         result = heap.delete()
#         print(result[1])
#         # heap.Print()

############################################################

# heapq모듈 사용 168ms
import heapq

heap = []
N = int(input())
for _ in range(N):
    M = int(input())
    if M:
        heapq.heappush(heap, (abs(M), M))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)